# put your python code here
a = input().lower().split()
b = ['ь','ъ','ы']

c = 1
for x in range(1,len(a)):
    if a[x][0] != a[x-1][-2 if a[x-1][-1] in b else -1]:
        c*=0
        print(a[x][0], a[x-1][-2 if a[x-1][-1] in b else -1])
print('ДА' if c else 'НЕТ')




