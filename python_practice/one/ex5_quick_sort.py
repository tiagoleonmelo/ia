def quick_sort(l):

    if len(l) <= 1:
        return l

    pivot = l[0]
    lst = l[:]

    smaller, larger = helper(pivot, lst[1:])

    return quick_sort(smaller) + [pivot] + quick_sort(larger)


def helper(elem, l):
    if l == []:
        return [[],[]]

    call = helper(elem, l[1:])

    if l[0] < elem:
        return [ call[0] + [l[0]], call[1] ]

    return [ call[0], call[1] + [l[0]] ]


l = [1, 3, 2, 8329, -1, 382, 5, -420]

print(quick_sort(l))


