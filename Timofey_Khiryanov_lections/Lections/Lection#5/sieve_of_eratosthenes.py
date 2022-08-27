from tkinter import N


N = 100
A = [True] * N
A[0] = A[1] = False
for k in range(2,N):
    for m in range(2*k,N,k):
        A[m] = False

for k in range(N):
    print(k,'-','простое' if A[k] else 'составное')