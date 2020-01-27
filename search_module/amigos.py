from constraintsearch import *

def amigo_constraint(v1, x1, v2, x2):
    return x1[0] != x2[0] and x1[1] != x2[1]

def self_constraint(v1, x1):
    print(v1, x1)
    print(x1[0][-1])
    return v1 == x1[0][-1] or v1 == x1[1][-1]


variables = ['a','b','c']

## Array de tuplos (bicicleta, chapeu)
values = [(str('bicicleta_' + x), str('chapeu_' + x)) for x in variables]

domains = {
            'a' : [('bicicleta_c', 'chapeu_b'), ('bicicleta_b', 'chapeu_c')],
            'b' : [('bicicleta_c', 'chapeu_a'), ('bicicleta_a', 'chapeu_c')],
            'c' : [('bicicleta_a', 'chapeu_b'), ('bicicleta_b', 'chapeu_a')]    
        }

edges = [
            ('a', 'b'), ('b', 'c') , ('c', 'a'),
            ('b', 'a'), ('c', 'b') , ('a', 'c') 
        ]

## Associar cada edge a amigo constraint
graph = { e: amigo_constraint for e in edges }

amigos = ConstraintSearch(domains, graph)

print(amigos.search())


