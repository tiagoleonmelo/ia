
# Modulo: tree_search
# 
# Fornece um conjunto de classes para suporte a resolucao de 
# problemas por pesquisa em arvore:
#    SearchDomain  - dominios de problemas
#    SearchProblem - problemas concretos a resolver 
#    SearchNode    - nos da arvore de pesquisa
#    SearchTree    - arvore de pesquisa, com metodos para 
#                    a respectiva construcao
#
#  (c) Luis Seabra Lopes
#  Introducao a Inteligencia Artificial, 2012-2018,
#  Inteligência Artificial, 2014-2018

from abc import ABC, abstractmethod

# Dominios de pesquisa
# Permitem calcular
# as accoes possiveis em cada estado, etc
class SearchDomain(ABC):

    # construtor
    @abstractmethod
    def __init__(self):
        pass

    # lista de accoes possiveis num estado
    @abstractmethod
    def actions(self, state):
        pass

    # resultado de uma accao num estado, ou seja, o estado seguinte
    @abstractmethod
    def result(self, state, action):
        pass

    # custo de uma accao num estado
    @abstractmethod
    def cost(self, state, action):
        pass

    # custo estimado de chegar de um estado a outro
    @abstractmethod
    def heuristic(self, state, goal_state):
        pass

# Problemas concretos a resolver
# dentro de um determinado dominio
class SearchProblem:
    def __init__(self, domain, initial, goal):
        self.domain = domain
        self.initial = initial
        self.goal = goal
    def goal_test(self, state):
        return state == self.goal

# Nos de uma arvore de pesquisa
class SearchNode:
    def __init__(self, state, parent, cost, heuristic): 
        self.state = state
        self.parent = parent
        if parent != None:
            self.depth = parent.depth+1
            self.acum_cost = parent.acum_cost + cost
        else:
            self.depth = 0
            self.acum_cost = 0

        self.heuristic = heuristic

    def __str__(self):
        return "no(" + str(self.state) + "," + str(self.parent) + ")"
    def __repr__(self):
        return str(self)

# Arvores de pesquisa
class SearchTree:

    # construtor
    def __init__(self,problem, strategy='breadth'): 
        self.problem = problem
        root = SearchNode(problem.initial, None, 0, 0)
        self.root = root
        self.open_nodes = [root]
        self.closed_nodes = []
        self.strategy = strategy
        self.sol_length = 0
        self.default_limit = 10
        self.total_nodes = 1
        self.terminais = 0
        self.nao_terminais = 0
        self.sol_acum_cost = 0
        self.highest_cost = [root]
        self.avg_depth = 0

    # obter o caminho (sequencia de estados) da raiz ate um no
    def get_path(self,node):
        if node.parent == None:
            return [node.state]
        path = self.get_path(node.parent)
        path += [node.state]
        return(path)

    # procurar a solucao
    def search(self):
        while self.open_nodes != []:
            node = self.open_nodes.pop(0)


            if self.problem.goal_test(node.state): # found the solution


                ## Length of the solution
                self.sol_length = node.depth
                print("Numero de transiçoes: ", self.sol_length)

                
                ## Total nodes ran
                print("Nós percorridos: ", self.total_nodes)


                ## Terminal Nodes are the nodes left open when the solution is found
                self.terminais = len(self.open_nodes)
                print("Nós terminais: ", self.terminais)


                ## Non-terminal Nodes are the remaining ones
                self.nao_terminais = self.total_nodes - self.terminais
                print("Nós não terminais: ", self.nao_terminais)


                ## Average ramification: ratio between the nodes ran (- 1 cuz root) and non-terminal nodes
                # On average, each nodes ramifies into <avg_ram> nodes
                avg_ram = (self.total_nodes-1) / self.nao_terminais
                print("Rácio de ramificação: ", avg_ram)

                
                ## Accumulated cost of the solution found
                self.sol_acum_cost = node.acum_cost
                print("Custo da solução: ", self.sol_acum_cost)


                ## Node with highest cost found
                print("Maior custo: ", self.highest_cost[0].acum_cost)


                ## Average depth of each node
                print("Profundidade média: ", self.avg_depth/self.total_nodes)


                return self.get_path(node)


            lnewnodes = []

            if node.depth > self.default_limit:
                continue
            
            
            for a in self.problem.domain.actions(node.state):
                newstate = self.problem.domain.result(node.state,a)

                if newstate not in self.get_path(node):
                    lnewnodes += [SearchNode(newstate,node,
                                            self.problem.domain.cost(node.state, (node.state, newstate)),
                                            self.problem.domain.heuristic(newstate, self.problem.goal))]
                    self.total_nodes += 1

                    if lnewnodes[-1].acum_cost > self.highest_cost[0].acum_cost:
                        self.highest_cost[0] = lnewnodes[-1]

                    self.avg_depth += lnewnodes[-1].depth

            self.add_to_open(lnewnodes)
        return None



    # juntar novos nos a lista de nos abertos de acordo com a estrategia
    def add_to_open(self,lnewnodes):
        if self.strategy == 'breadth':
            self.default_limit = 190190910
            self.open_nodes.extend(lnewnodes)
        elif self.strategy == 'depth':
            self.default_limit = 19201920
            self.open_nodes[:0] = lnewnodes
        elif self.strategy == 'uniform':
            ## Uniform search: f(n) = accumumlated_cost(n)
            # Sort by acum_cost(node)
            self.open_nodes.extend(lnewnodes)
            self.open_nodes = sorted(self.open_nodes, key = lambda x: x.acum_cost)           
        elif self.strategy == 'greedy':
            ## Greedy search: f(n) = heuristic(n)
            # Sort by heuristic(node)         
            self.open_nodes.extend(lnewnodes)
            self.open_nodes = sorted(self.open_nodes, key = lambda x: x.heuristic)
        elif self.strategy == 'astar':
            ## Greedy search: f(n) = accumumlated_cost(n) + heuristic(n)
            # Sort by acum_cost(node) + heuristic(node)         
            self.open_nodes.extend(lnewnodes)
            self.open_nodes = sorted(self.open_nodes, key = lambda x: x.acum_cost + x.heuristic)

