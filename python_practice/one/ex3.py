# Funçoes que retornam None
import math

def head(l):
    if l == []:
        return None

    return l[0]


def tail(l):
    if l == [] or len(l) == 1:
        return None

    return l[1:]


def homologos(l1, l2):
    if l1 == []:
        return []

    return [(l1[0],l2[0])]+homologos(l1[1:], l2[1:])


def min_finder(l):
    if l == []:
        return None

    if len(l) == 1:
        return l[0]

    next_min = min_finder(l[1:])

    if next_min != None and l[0] < next_min:
        return l[0]

    return next_min


def separar_min(l):
    sl = sorted(l)
    return (sl[0], tail(sl))
    

def max_finder(l):
    if l == []:
        return None

    if len(l) == 1:
        return l[0]

    next_max = max_finder(l[1:])

    if next_max != None and l[0] > next_max:
        return l[0]

    return next_max


def min_max(l):
    return (min_finder(l), max_finder(l))


def separar_min_v2(l):
    sl = sorted(l)
    return (sl[0], sl[1], sl)


def avg_calc(l):
    soma, conta = sum_and_count(l)
    return (soma/conta, l[int(math.floor(conta/2))])

def sum_and_count(l):
    if l == []:
        return (0, 0)

    return (l[0] + sum_and_count(l[1:])[0], 1 + sum_and_count(l[1:])[1])



l = [2,3,4,5,1]
l2 = [2,3,4,5,2]
empty = []

print(head(l))
print(tail(l))
print(min_finder(l))
print(separar_min(l))
print(min_max(l))

print(avg_calc(l))

print(homologos(l,l2))
