a = ['a','b','v','d']
b = [[]]
for i in range(1,len(a)+1):
    for j in range(0,len(a)-i+1,1):
        b.append(a[j:j+i])
print(b)