
from bayes_net import *

# Exemplo dos acetatos:

bn = BayesNet()

# bn.add('r',[],0.001)
# bn.add('t',[],0.002)

# bn.add('a',[('r',True ),('t',True )],0.950)
# bn.add('a',[('r',True ),('t',False)],0.940)
# bn.add('a',[('r',False),('t',True )],0.290)
# bn.add('a',[('r',False),('t',False)],0.001)

# bn.add('j',[('a',True )],0.900)
# bn.add('j',[('a',False)],0.050)

# bn.add('m',[('a',True )],0.700)
# bn.add('m',[('a',False)],0.100)

# conjunction = [('j',True),('m',True),('a',True),('r',False),('t',False)]


bn.add('s', [], 0.6)
bn.add('pal', [], 0.05)

bn.add('m', [('s', False)], 0.001)
bn.add('m', [('s', True)], 0.9)

bn.add('a', [('pal', True)], 0.25)
bn.add('a', [('pal', False)], 0.004)

bn.add('cp', [('s', True), ('a', False)], 0.01)
bn.add('cp', [('s', True), ('a', True)], 0.02)
bn.add('cp', [('s', False), ('a', False)], 0.001)
bn.add('cp', [('s', False), ('a', True)], 0.011)

bn.add('f', [('pal', False), ('a', False)], 0.01)
bn.add('f', [('pal', False), ('a', True)], 0.1)
bn.add('f', [('pal', True)], 0.9)

conjunction = [('s', True), ('a', True), ('pal', True), ('m', True), ('cp', True), ('f', True)]
conjunctiont = [('s', False), ('a', False), ('pal', False), ('m', False), ('cp', False), ('f', False)]

print(bn.jointProb(conjunction))
print(bn.jointProb(conjunctiont))


print(bn.individual_prob('a', True))

