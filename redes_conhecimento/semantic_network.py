from collections import Counter

# Guiao de representacao do conhecimento
# -- Redes semanticas
# 
# Inteligencia Artificial & Introducao a Inteligencia Artificial
# DETI / UA
#
# (c) Luis Seabra Lopes, 2012-2020
# v1.9 - 2019/10/20
#


# Classe Relation, com as seguintes classes derivadas:
#     - Association - uma associacao generica entre duas entidades
#     - Subtype     - uma relacao de subtipo entre dois tipos
#     - Member      - uma relacao de pertenca de uma instancia a um tipo
#

class Relation:
    def __init__(self,e1,rel,e2):
        self.entity1 = e1
#       self.relation = rel  # obsoleto
        self.name = rel
        self.entity2 = e2
    def __str__(self):
        return self.name + "(" + str(self.entity1) + "," + \
               str(self.entity2) + ")"
    def __repr__(self):
        return str(self)


# Subclasse Association
class Association(Relation):
    def __init__(self,e1,assoc,e2):
        Relation.__init__(self,e1,assoc,e2)

#   Exemplo:
#   a = Association('socrates','professor','filosofia')

# Subclasse Subtype
class Subtype(Relation):
    def __init__(self,sub,super):
        Relation.__init__(self,sub,"subtype",super)


#   Exemplo:
#   s = Subtype('homem','mamifero')

# Subclasse Member
class Member(Relation):
    def __init__(self,obj,type):
        Relation.__init__(self,obj,"member",type)

#   Exemplo:
#   m = Member('socrates','homem')

class AssocOne(Relation):
    def __init__(self,e1,assoc,e2):
        Relation.__init__(self,e1,assoc,e2)

class AssocNum(Relation):
    def __init__(self,e1,assoc,e2):
        Relation.__init__(self,e1,assoc,float(e2))

# classe Declaration
# -- associa um utilizador a uma relacao por si inserida
#    na rede semantica
#
class Declaration:
    def __init__(self,user,rel):
        self.user = user
        self.relation = rel
    def __str__(self):
        return "decl("+str(self.user)+","+str(self.relation)+")"
    def __repr__(self):
        return str(self)

#   Exemplos:
#   da = Declaration('descartes',a)
#   ds = Declaration('darwin',s)
#   dm = Declaration('descartes',m)

# classe SemanticNetwork
# -- composta por um conjunto de declaracoes
#    armazenado na forma de uma lista
#
class SemanticNetwork:
    def __init__(self,ldecl=[]):
        self.declarations = ldecl
    def __str__(self):
        return my_list2string(self.declarations)
    def insert(self,decl):
        self.declarations.append(decl)
    def query_local(self,user=None,e1=None,rel=None,e2=None):
        self.query_result = \
            [ d for d in self.declarations
                if  (user == None or d.user==user)
                and (e1 == None or d.relation.entity1 == e1)
                and (rel == None or d.relation.name == rel)
                and (e2 == None or d.relation.entity2 == e2) ]
        return self.query_result
    def show_query_result(self):
        for d in self.query_result:
            print(str(d))


    ## 1 - Lista de associaçoes existentes
    def get_assocs(self):
        return list(set([d.relation.name for d in self.declarations if isinstance(d.relation, Association)]))


    ## 2 - Lista de instancias de tipos
    def get_type_inst(self):
        return list(set([d.relation.entity1 for d in self.declarations if isinstance(d.relation, Member)]))


    ## 3 - Lista de utilizadores existentes na rede
    def get_users(self):
        return list(set([d.user for d in self.declarations]))


    ## 4 - Lista de tipos existentes na rede
    def get_types(self):
        return list(set([d.relation.entity2 for d in self.declarations if isinstance(d.relation, Subtype)])) + list(set([d.relation.entity1 for d in self.declarations if isinstance(d.relation, Subtype)]))


    ## 5 - Lista de associaçoes localmente declaradas de uma entidade
    def get_entity_assocs(self, entity):
        return list(set([d.relation.name for d in self.declarations if isinstance(d.relation, Association) and d.relation.entity1 == entity]))


    ## 6 - Lista de declaraçoes feitas por um user
    def get_user_decls(self, user):
        return [d for d in self.declarations if d.user == user]


    ## 7 - Numero de associaçoes usadas nas relaçoes
    def get_diff_assocs_num(self, user):
        return len(list(set([d.relation.name for d in self.declarations if d.user == user and isinstance(d.relation, Association)])))


    ## 8 - Lista de Tuplos (associaçao, user) onde entity entra na associaçao
    def get_assoc_users(self, entity):
        return list(set([(d.relation.name, d.user) for d in self.declarations if d.relation.entity1 == entity or d.relation.entity2 == entity]))


    ## 9 - Devolve se e1 é predecessor de e2
    def predecessor(self, e1, e2):
        check = [d for d in self.declarations if d.relation.entity1 == e2 and d.relation.entity2 == e1 and not isinstance(d.relation, Association)]
        if check != []:
            return True

        return any([self.predecessor(e1, d.relation.entity2) for d in self.declarations if not isinstance(d.relation, Association) and d.relation.entity1 == e2])


    ## 10 - Cadeia de predecessores onde e1 é predecessor de e2
    def predecessor_chain(self, e1, e2):

        if not self.predecessor(e1, e2):
            return None

        parents = [d.relation.entity2 for d in self.declarations if (d.relation.entity1 == e2) and not isinstance(d.relation, Association)]

        if e1 in parents:
            return [e1, e2]

        for p in parents:
            t = self.predecessor_chain(e1, p)
            if t:
                return t + [e2]

    ## 11a - Query de assocs herdadas e locais
    def query(self, entity, assoc=None):
        inherited = [self.query(d.relation.entity2, assoc) for d in self.declarations if d.relation.entity1 == entity and not isinstance(d.relation, Association)]
        return [item for sublist in inherited for item in sublist] + self.query_local(e1=entity, rel=assoc)

    ## 11b - Query 
    def query2(self, entity, assoc=None):
        inherited = [self.query2(d.relation.entity2, assoc) for d in self.declarations if d.relation.entity1 == entity and not isinstance(d.relation, Association)]
        local = [d for d in self.declarations if d.relation.entity1 == entity]

        return [item for sublist in inherited for item in sublist if isinstance(item.relation, Association)] + local


    ## 12 - Herda, no maximo, de 1 entidade
    def query_cancel(self, entity, assoc):
        local = self.query_local(e1 = entity, rel = assoc)
        if local:
            return local

        ret = [self.query_cancel(d.relation.entity2, assoc) for d in self.declarations if d.relation.entity1 == entity and not isinstance(d.relation, Association)]
        return [item for sublist in ret for item in sublist]

    ## 13 - Obter children de um parent com associaçoes assoc
    def query_down(self, entity, assoc, skip=True):
        children = [self.query_down(d.relation.entity1, assoc, False) for d in self.declarations if not isinstance(d.relation, Association) and d.relation.entity2 == entity]

        if skip:
            l = []
        else:
            l = self.query_local(e1=entity, rel=assoc)

        return [item for sublist in children for item in sublist] + l

    ## 14 - Query q devolve o valor mais provavel
    def query_induce(self, entity, assoc):
        cnt = Counter()
        children = self.query_down(entity, assoc)

        for c in children:
            cnt[c.relation.entity2] += 1

        return cnt.most_common(1)[0]
        

    ## 15
    def query_local_assoc(self, entity, assoc):
        local = self.query_local(e1=entity, rel=assoc)
        cnt = Counter()
        counter = 0

        if isinstance(local[0].relation, AssocOne):
            for l in local:
                cnt[l.relation.entity2] += 1
                counter += 1

            return (cnt.most_common(1)[0][0], cnt.most_common(1)[0][1]/counter)


# Funcao auxiliar para converter para cadeias de caracteres
# listas cujos elementos sejam convertiveis para
# cadeias de caracteres
def my_list2string(list):
   if list == []:
       return "[]"
   s = "[ " + str(list[0])
   for i in range(1,len(list)):
       s += ", " + str(list[i])
   return s + " ]"
    

