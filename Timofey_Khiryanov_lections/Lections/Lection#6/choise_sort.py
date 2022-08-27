A = [4,2,5,1,3]

for x in range(len(A)-1):
    print('цикл №',x)
    for k in range(x,len(A),1):
        if A[x] > A[k]: # по возрастанию
            A[k], A[x] = A[x], A[k]

print(A)

A = [4,2,5,1,3]

for x in range(len(A)-1):
    for k in range(x,len(A),1):
        if A[x] < A[k]: # по убыванию
            A[k], A[x] = A[x], A[k]

print(A)