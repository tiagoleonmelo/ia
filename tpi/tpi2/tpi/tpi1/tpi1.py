

from tree_search import *

class MyTree(SearchTree):

    def __init__(self,problem, strategy='breadth',max_nodes=None): 
        #IMPLEMENT HERE
        pass

    def astar_add_to_open(self,lnewnodes):
        #IMPLEMENT HERE
        pass

    def effective_branching_factor(self):
        #IMPLEMENT HERE
        pass

    def update_ancestors(self,node):
        #IMPLEMENT HERE
        pass

    def discard_worse(self):
        #IMPLEMENT HERE
        pass

    def search2(self):
        #IMPLEMENT HERE
        pass

    # shows the search tree in the form of a listing
    def show(self,heuristic=False,node=None,indent=''):
        if node==None:
            self.show(heuristic,self.root)
            print('\n')
        else:
            line = indent+node.state
            if heuristic:
                line += (' [' + str(node.evalfunc) + ']')
            print(line)
            if node.children==None:
                return
            for n in node.children:
                self.show(heuristic,n,indent+'  ')



