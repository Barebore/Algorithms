N = 50
A = [0] * N
B = [0] * N
for k in range(N):
    A[k] = k+1
print(A)
for k in range(N):
    B[k] = A[k]
print(B)
C = A 
A[0] = 777
print(C[0])
D = list(A) # явный вызов конструктора массива
A[0] = 555
print(D[0])
############