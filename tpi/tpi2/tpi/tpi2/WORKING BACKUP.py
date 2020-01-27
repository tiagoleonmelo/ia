from collections import Counter
from functools import reduce

from semantic_network import *
from bayes_net import *

# 89005 - Tiago Melo

class MySN(SemanticNetwork):


    def query_dependents(self,entity):
        # returns a list of dependents ON entity
        dependants = [d.relation.entity1 for d in self.declarations if 
                            isinstance(d.relation, Depends) and d.relation.entity2 == entity]

        first_children = [d.relation.entity1 for d in self.declarations if
                            (isinstance(d.relation, Member) or isinstance(d.relation, Subtype))
                            and d.relation.entity2 == entity]
        
        l = [self.query_dependents(c) for c in first_children]
        l = [item for sublist in l for item in sublist]

        for p in dependants:
            # if p has any children
            # return [recursive call on children] + [children]
            # else
            # return [recursive call on p] + [p]

            children = [d.relation.entity1 for d in self.declarations if
                                        d.relation.entity2 == p and (isinstance(d.relation, Member) or isinstance(d.relation, Subtype))]

            if children:
                temp = [self.query_dependents(c) for c in children]
                l += [item for sublist in temp for item in sublist] + children

            else:
                l += self.query_dependents(p) + [p]
        
        return list(set(l))
        

    def query_causes(self, entity, skip=True):
        # fetching every dependency/parent
        desc = [self.query_causes(d.relation.entity2, False) for d in self.declarations if
                        d.relation.entity1 == entity and not isinstance(d.relation, Association)]

        # merging into one list
        desc = [item for sublist in desc for item in sublist]

        # getting every parent
        parents = [d.relation.entity2 for d in self.declarations if 
                                (isinstance(d.relation, Subtype) or isinstance(d.relation, Member))]

        # filtering results
        ret = [d for d in desc if d not in parents]

        # skipping the first entity
        if skip:
            return list(set(ret))

        return list(set(ret + [entity]))


    def query_causes_sorted(self,entity):
        # calcular a average de each fixing cost for each user
        causes = self.query_causes(entity)
        ret = []

        for c in causes:

            # ir buscar todos os tempos associados a cada causa
            debug_times = [d.relation.entity2 for d in self.declarations if d.relation.name == 'debug_time' and d.relation.entity1 == c]

            # no caso de nao haver registos de debug times para a causa c
            if debug_times:
            # dar append a um tuplo (causa, media(debug_time))
                ret += [(c,  reduce(lambda x, y: x + y, debug_times) / len(debug_times) )]
        
        # sort de acordo com o segundo elemento de cada tuplo
        # sort twice to break ties
        ret.sort(key=lambda x : x[0])
        ret.sort(key=lambda x : x[1])
        return ret


class MyBN(BayesNet):

    def markov_blanket(self,var):
        # fetch var's parents
        # fetch var's children
        # fetch var's children's parents
        #
        # put the whole thing together
        # list(set(thing))

        parents = self.parent_calculator(var)
        children = [d for d in self.dependencies if var in self.parent_calculator(d)]
        other_parents = [p for d in self.dependencies for p in self.parent_calculator(d) 
                                if p != var and var in self.parent_calculator(d)]

        return list(set(parents + children + other_parents))

    # returns a list of parents for variable key
    def parent_calculator(self, key):
        return list(set([item[0] for sublist in [list(fs) for fs in list(self.dependencies[key])] for item in sublist]))
