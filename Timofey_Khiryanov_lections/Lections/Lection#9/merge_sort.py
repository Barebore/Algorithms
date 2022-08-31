def merge(A:list, B:list):
    i = k = n = 0
    C = [0] * (len(A)+len(B))
    while i < len(A) and k < len(B):
        if A[i] <= B[k]:
            C[n] = A[i]
            n += 1
            i += 1
        else:
            C[n] = B[k]
            n += 1
            k += 1
    while i < len(A):
        C[n] = A[i]
        n += 1
        i += 1
    while k < len(B):
        C[n] = B[k]
        n += 1
        k += 1
    return C

def merge_sort(A):
    if len(A) <= 1:
        return
    middle = len(A) // 2
    L = [A[i] for i in range(0, middle)]
    R = [A[i] for i in range(middle, len(A))]
    print(*L)
    print(*R)
    merge_sort(L)
    merge_sort(R)
    C = merge(L,R)
    for i in range(len(A)):
        A[i] = C[i]

A = [1,2,3,4,5,6]
merge_sort(A)
print(*A)