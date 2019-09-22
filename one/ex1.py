# Funçoes para processamento de listas

def size_lista(lista, i=0):
    if lista==[]:
        return 0
    return 1 + size_lista(lista[1:])


def sum_list(lista):
    if lista == []:
        return 0
    return lista[0] + sum_list(lista[1:])


def listContains(element, lista):
    if lista == []:
        return False
    elif lista[0] == element:
        return True

    return listContains(element, lista[1:])


def listConcat(list_a, list_b):
    if list_a == []:
        return list_b
    c = listConcat(list_a[1:], list_b)
    c[:0] = [list_a[0]]
    return c


def listReversal(lista):
    if lista == []:
        return []
    return [lista[-1]]+listReversal(lista[:-1])


def isCapicua(lista):
    if listReversal(lista) == lista:
        return True
    return False


def bigListConcat(lista_grande):
    if lista_grande == []:
        return []
    return lista_grande[0]+bigListConcat(lista_grande[1:])


def replace(l, x, y):
    if l == []:
        return []
    
    elif l[0] == x:
        l[0] = y

    return [l[0]]+replace(l[1:], x, y)


def merge(l1, l2):
    if l1 == [] and l2 == []:
        return []

    if not l1:
        return l2

    if not l2:
        return l1

    if l1[0] <= l2[0]:
        return [l1[0]]+merge(l1[1:], l2)
    else:
        return [l2[0]]+merge(l1, l2[1:])

def subset(set):
    if not set:
        return [set]
    rest = subset(set[1:])
    return rest + [[set[0]] + item for item in rest]







lista = ['a','b','c','d','e']
nums = [1, 2, 3, 4, 5,163,170,200]
reversable = [1,2,3,162,164,201]
capicua = ['a','n','a']
a = [1,2,3]
big_list = [lista, nums, reversable, capicua]

print(size_lista(lista))

print(sum_list(nums))

print(listContains('r', lista))
print(listContains(1, nums))

#print(listConcat(lista, nums))

print(listReversal(reversable))

print(isCapicua(capicua))

print(bigListConcat(big_list))

print(replace(nums, 2, 64))

print(merge(nums,reversable))

print(subset(a))


