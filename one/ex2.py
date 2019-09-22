# Funções para processamento de listas e tuplos

def separar(tuple_list):
    if tuple_list == []:
        return ([],[])

    return ( [tuple_list[0][0]] + separar(tuple_list[1:])[0], [tuple_list[0][1]] + separar(tuple_list[1:])[1] )

def remove_e_conta(l, x):
    if l == []:
        return ([], 0)

    if l[0] == x:
        l.pop(0)
        rec = remove_e_conta(l,x)
        return (rec[0], rec[1] + 1)

    rec = remove_e_conta(l[1:],x)

    return ([l[0]] + rec[0], rec[1])

def element_counter(l):
    if l == []:
        return []

    rec = element_counter(l[1:])

    if exists(rec,l[0]):
        idx = idx_finder(rec,l[0])
        tpl = rec.pop(idx)
        rec.append((tpl[0],tpl[1]+1))
    else:
        rec.append((l[0],1))

    return rec

# Helper functions

# Returns true if x is the first element of any tuple in list l
def exists(l, x):
    if l == []:
        return False

    if l[0][0] == x:
        return True

    return exists(l[1:], x)


# Returns the position of x in list l
def idx_finder(l, x):
    if l[0][0] == x:
        return 0

    return 1 + idx_finder(l[1:], x)

    

l = [(0,1),(0,1),(0,1),(0,1),(0,1)]
lx = [1,2,3,4,5,6,6,6,6,6,6,6,6,6]

print(separar(l))
print(remove_e_conta(lx,6))
print(element_counter(lx))