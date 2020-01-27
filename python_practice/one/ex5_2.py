def selection_sort(l, f):

    if len(l) == 1:
        return l

    lst = l[:]
    idx = l.index(min_index(l, f))

    if idx != 0:
        lst[0], lst[idx] = lst[idx], lst[0]

    return [lst[0]]+selection_sort(lst[1:])



def bubble_sort(l, f):

    if len(l) == 1:
        return l

    lst = l[:]

    if f(l[0], l[1]):
        lst[0], lst[1] = l[1], l[0]
        
    ret = [lst[0]] + bubble_sort(lst[1:])

    if lst != ret:
        ret = bubble_sort(ret)

    return ret



def quick_sort(l, f):

    if len(l) <= 1:
        return l

    pivot = l[0]
    lst = l[:]

    smaller, larger = helper(pivot, lst[1:], f)

    return quick_sort(smaller) + [pivot] + quick_sort(larger)



## Helper functions

def min_index(l, f):
    if l == []:
        return None

    if len(l) == 1:
        return l[0]

    mini = min_index(l[1:])

    if f(l[0], mini):
        return l[0]
    
    return mini

def helper(elem, l, f):
    if l == []:
        return [[],[]]

    call = helper(elem, l[1:])

    if f(l[0], elem):
        return [ call[0] + [l[0]], call[1] ]

    return [ call[0], call[1] + [l[0]] ]


