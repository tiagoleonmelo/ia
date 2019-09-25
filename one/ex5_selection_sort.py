def selection_sort(l):

    if len(l) == 1:
        return l

    lst = l[:]
    idx = l.index(min_index(l))

    if idx != 0:
        lst[0], lst[idx] = lst[idx], lst[0]

    return [lst[0]]+selection_sort(lst[1:])


def min_index(l):
    if l == []:
        return None

    if len(l) == 1:
        return l[0]

    mini = min_index(l[1:])

    if l[0] < mini:
        return l[0]
    
    return mini


l = [-1,1,2,3,0]

print(selection_sort(l))