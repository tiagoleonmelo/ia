# Funçoes lambda
import math
import operator
import functools

# Lambda Functions
isEven = lambda x : False if x % 2 == 1 else True
isPositive = lambda x : True if x > 0 else False
bigger = lambda x,y : True if abs(x) < abs(y) else False
polarConverter = lambda xy : (math.sqrt(xy[0]**2+xy[1]**2), math.tan(xy[1]/xy[0]))

def big_mess(f,g,h):
    ret = lambda x,y,z : h(f(x,y),g(y,z))
    return ret


def quant_univ_every_true(l,f):
    l1 = list(filter(f, l))

    if l1 != l:
        return False

    return True


def quant_univ_at_least_one_true(l,f):
    l1 = list(filter(f, l))

    if not l1:
        return False

    return True


def subset_check(l1,l2):
    check = lambda x,l : True if x in l else False
    
    if not l1:
        return True

    if not check(l1[0], l2):
        return False

    return subset_check(l1[1:],l2)


def minor_w_reduce(l, f):
    if len(l)<1:
        return None
    if len(l)==1:
        return l[0]
    else:
        return functools.reduce( lambda x, y : x if f(x,y) else y,l)


def minor_w_reduce_separa(l, f):
    if len(l)<1:
        return None
    if len(l)==1:
        return (l[0],[])
    else:
        min_=functools.reduce( lambda x, y : x if f(x,y) else y,l)
        list1=list(filter(lambda x: x!= min_, l))
        return (min_, list1)

    
def double_min_finder(l, f):
    if len(l)<2:
        return None
    if len(l)==2:
        return (l[0],l[1],[])
    
    min_1 = functools.reduce( lambda x,y : x if f(x,y) else y, l)
    temp = list(filter(lambda x : x != min_1, l))
    min_2 = functools.reduce( lambda x,y : x if f(x,y) else y, temp)
    ret = list(filter(lambda x : x != min_2, temp))

    return (min_1, min_2, ret)


def list_converter(l):
    return list(map(polarConverter,l))


def merge_lists(l1, l2, f):
    if not l1 and not l2:
        return []

    if not l1:
        return l2

    if not l2:
        return l1

    if f(l1[0], l2[0]):
        return [l1[0]]+merge_lists(l1[1:],l2,f)

    return [l2[0]]+merge_lists(l1,l2[1:],f)

def conc_aplic(l, f):
    
    if not l:
        return []

    x = list(map(f, l[0]))

    x.extend(conc_aplic(l[1:],f))

    return x

def aplic_combin(t, f):
    if len(t[0]) != len(t[1]):
        return None
    return list(map(f, t[0], t[1]))

def list_of_lists(l, f, elem):
    if l == []:
        return elem
    return [functools.reduce(f, l[0])]+list_of_lists(l[1:], f, elem)


    


# Tester functions

def smaller_num(x,y):
    return x < y

def sum_(x,y):
    return x+y

def sub(x,y):
    return x-y

def mult(x,y):
    return x*y

def identity(x):
    return 1

# Driver code

l_1 = [1,2,3,4,5,6,7]
l_2 = [2,4,6]
l_3 = [(2,3),(3,4)]
l_4 = [[0,2,3,4],[5,6,7]]
l_5 = ([1,2,3,4],[1,2,3,4])

print(isEven(2))

print(isPositive(2109))

print(bigger(2,3))

print(polarConverter((4,3)))

expr = big_mess(sum_,sub,mult)
print(expr(2,3,1))

print(quant_univ_at_least_one_true(l_1,isEven))

print(quant_univ_every_true(l_1,isEven))

print(subset_check(l_2,l_1))

print(minor_w_reduce(l_2, smaller_num))

print(minor_w_reduce_separa(l_2, smaller_num))

print(double_min_finder(l_2, smaller_num))

print(list_converter(l_3))

print(merge_lists(l_1,l_2,smaller_num))

print(conc_aplic(l_4,identity))

print(aplic_combin(l_5, sum_))

print(list_of_lists(l_4, operator.add, 0))