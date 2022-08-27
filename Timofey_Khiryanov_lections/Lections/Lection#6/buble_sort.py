A = [4,2,5,1,3]

for x in range(1,len(A)):
    print('cycle #',x)
    for k in range(len(A)-x):
        print('cycle # k =',k)
        if A[k] > A[k+1]:
            A[k], A[k+1] = A[k+1], A[k]

print(A)