



# Redes semanticas
# -- Exemplo
# 
# Inteligencia Artificial & Introducao a Inteligencia Artificial
# DETI / UA
#
# (c) Luis Seabra Lopes, 2012-2019
# 2019/10/20
#


from semantic_network import *

a = Association('socrates','professor','filosofia')
s = Subtype('homem','mamifero')
m = Member('socrates','homem')

da = Declaration('descartes',a)
ds = Declaration('darwin',s)
dm = Declaration('descartes',m)

z = SemanticNetwork()
z.insert(da)
z.insert(ds)
z.insert(dm)
z.insert(Declaration('darwin',Association('mamifero','mamar','sim')))
z.insert(Declaration('darwin',Association('homem','gosta','carne')))

# novas declaracoes

z.insert(Declaration('darwin',Subtype('mamifero','vertebrado')))
z.insert(Declaration('descartes', Member('aristoteles','homem')))

b = Association('socrates','professor','matematica')
z.insert(Declaration('descartes',b))
z.insert(Declaration('simao',b))
z.insert(Declaration('simoes',b))

z.insert(Declaration('descartes', Member('platao','homem')))

e = Association('platao','professor','filosofia')
z.insert(Declaration('descartes',e))
z.insert(Declaration('simao',e))

z.insert(Declaration('descartes',Association('mamifero','altura',1.2)))
z.insert(Declaration('descartes',Association('homem','altura',1.75)))
z.insert(Declaration('simao',Association('homem','altura',1.85)))
z.insert(Declaration('darwin',Association('homem','altura',1.75)))

z.insert(Declaration('descartes', Association('socrates','peso',80)))
z.insert(Declaration('darwin', Association('socrates','peso',75)))
z.insert(Declaration('darwin', Association('platao','peso',75)))


z.insert(Declaration('damasio', Association('filosofo','gosta','filosofia')))
z.insert(Declaration('damasio', Member('socrates','filosofo')))


# Extra - descomentar as restantes declaracoes para o exercicio II.2.16

z.insert(Declaration('descartes', AssocNum('socrates','pulsacao',51)))
z.insert(Declaration('darwin', AssocNum('socrates','pulsacao',61)))
z.insert(Declaration('darwin', AssocNum('platao','pulsacao',65)))

z.insert(Declaration('descartes',AssocNum('homem','temperatura',36.8)))
z.insert(Declaration('simao',AssocNum('homem','temperatura',37.0)))
z.insert(Declaration('darwin',AssocNum('homem','temperatura',37.1)))
z.insert(Declaration('descartes',AssocNum('mamifero','temperatura',39.0)))

z.insert(Declaration('simao',Association('homem','gosta','carne')))
z.insert(Declaration('darwin',Association('homem','gosta','peixe')))
z.insert(Declaration('simao',Association('homem','gosta','peixe')))
z.insert(Declaration('simao',Association('homem','gosta','couves')))

z.insert(Declaration('damasio', AssocOne('socrates','pai','sofronisco')))
z.insert(Declaration('darwin', AssocOne('socrates','pai','pericles')))
z.insert(Declaration('descartes', AssocOne('socrates','pai','sofronisco')))

print(z)

# 1
print(1, z.get_assocs())

# 2
print(2, z.get_type_inst())

# 3
print(3, z.get_users())

# 4
print(4, z.get_types())

# 5
print(5, z.get_entity_assocs('socrates'))

# 6
print(6, z.get_user_decls('simao'))

# 7
print(7, z.get_diff_assocs_num('simao'))

# 8
print(8, z.get_assoc_users('socrates'))

# 9
print(9, z.predecessor('vertebrado', 'socrates'))

# 10
print(10, z.predecessor_chain('vertebrado', 'socrates'))

# 11a
print("11a", z.query('socrates', 'altura'))

# 11b
print("11b", z.query2('homem'))

# 12
print(12, z.query_cancel('socrates', 'altura'))

# 13
print(13, z.query_down('mamifero', 'altura'))

# 14
print(14, z.query_induce('vertebrado', 'altura'))