A = [x**2 for x in range(-5,5,1)]
print(A)
B = []
B = [x**2 for x in B if x%2 == 0]
C = []
C = [(0 if x<0 else x**2) for x in A if x%2 == 0]
print(C)