def merge(a,b):
    i = j = n = 0
    c = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j +=1
    while i < len(a):
        c.append(a[i])
        i += 1
    while j < len(b):
        c.append(b[j])
        j += 1
    return c

def merge_sort(a):
    if len(a) <=1:
        return
    middle = len(a) // 2
    L = [a[i] for i in range(0,middle)]
    R = [a[i] for i in range(middle,len(a))]
    merge_sort(L)
    merge_sort(R)
    C = merge(L,R)
#    for i in range(len(a)):
#        a[i] = C[i]
    a[:] = C[:]
    return C

a = [1,4,10,11]
b = [2,3,3,4,8]
c = [1,2,3,4,3,2,1]


print(merge_sort(c))