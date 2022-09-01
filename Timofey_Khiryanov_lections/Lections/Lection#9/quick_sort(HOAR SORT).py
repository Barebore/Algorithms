def hoar_sort(A):
    if len(A) <= 1:
        return
    barrier = A[0]
    L = []
    M = []
    R = []
    for x in A:
        if x < barrier:
            L.append(x)
        elif x == A[0]:
            M.append(x)
        else:
            R.append(x)
    print('L =',L)
    print('M =',M)
    print('R =',R)
    hoar_sort(L)
    hoar_sort(R)
    k = 0
    for x in L+M+R:
        A[k] = x
        k += 1

A = [4,8,7,6,5,4,3,3,2,1,4,5,6,7,3,4,3,5,6,7,2,3,5,6,7,8]
hoar_sort(A)
print(*A)


for x in A:
    print(x)