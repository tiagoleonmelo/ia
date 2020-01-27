from functools import reduce

from semantic_network import *
from bayes_net import *

# 89005 - Tiago Melo

class MySN(SemanticNetwork):


    def query_dependents(self,entity):
            #IMPLEMENT HERE

            l=[] 
            dep=[]
            ret = []
            fc = []

            # get the local children
            for d in self.declarations:
                if isinstance(d.relation, Subtype):
                    if d.relation.entity2 == entity:
                        fc.append(d.relation.entity1)

            for c in fc:
                tl = self.query_dependents(c)
                for res in tl:
                    ret.append(res)


            for d in self.declarations:
                if isinstance(d.relation, Depends):
                    if d.relation.entity2==entity:
                        l.append(d.relation.entity1)

            for i in l:
                parent_flag = 0
                for d in self.declarations:
                    if isinstance(d.relation, Subtype) and d.relation.entity2==i: # means i is a parent
                        parent_flag = 1
                        children = []
                        for d in self.declarations:
                            if isinstance(d.relation, Subtype) and d.relation.entity2==i:
                                children += [d.relation.entity1]
                        t = []
                        for c in children:
                            t += self.query_dependents(c)
                        ret += t + children

                if parent_flag:
                    continue

                ret += self.query_dependents(i) + [i]

            return list(set(ret))
        

    def query_causes(self, entity, skip=True):
        # fetching every dependency/parent
        desc = [self.query_causes(d.relation.entity2, False) for d in self.declarations if
                        d.relation.entity1 == entity and not isinstance(d.relation, Association)]

        # merging into one list
        desc = [item for sublist in desc for item in sublist]

        # getting every parent
        parents = [d.relation.entity2 for d in self.declarations if isinstance(d.relation, Subtype)]

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