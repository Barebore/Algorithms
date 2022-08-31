def merge(A:list, B:list):
    i = k = n = 0
    C = [0] * (len(A)+len(B))
    while i <= len(A) and k <= len(B):
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
        C[n] = A[k]
        n += 1
        k += 1
    