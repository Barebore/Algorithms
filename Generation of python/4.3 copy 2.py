# put your python code here
a = input().replace(' ','')
b = [[a[0]]]
j = 0
for i in range(1,len(a)):
    if a[i] == a[i-1]:
        b[j].append(a[i])
    else:
        b.append([a[i]])
        j += 1

print(b)