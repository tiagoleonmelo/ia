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


# Finish this later
# def avg_calc(l):
#     if l == []:
#         return 0
    
#     if len(l) % 2 == 0:
#         return l[len(l)/2]

#     else:
#         return (l[math.ceil(len(l)/2)]+l[math.floor(len(l)/2)])/2



l = [2,3,4,5,1]
empty = []

print(head(l))
print(tail(l))
print(min_finder(l))
print(separar_min(l))
print(min_max(l))
