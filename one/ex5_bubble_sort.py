def bubble_sort(l):

    if len(l) == 1:
        return l

    lst = l[:]

    if l[0] > l[1]:
        lst[0], lst[1] = l[1], l[0]
        
    ret = [lst[0]] + bubble_sort(lst[1:])

    if lst != ret:
        ret = bubble_sort(ret)

    return ret


l = [3,2,5,1,24,54,23,53,0,-12,23]

print(bubble_sort(l))
print(l)