# put your python code here
a = ['+',7,'(', int, int, int, ')', int, int, int, '-',
    int, int, '-', int, int]
b = input()
c = []
d = 1
for x in b:
    try:
        c.append(int(x) if int(x) in [1,2,3,4,5,6,7,8,9,0] else x)
    except:
        c.append(x)
if len(c) == len(b) and len(b) == 16:
    for i in range(len(c)):
        if  c[i] != a[i] and type(c[i]) != a[i]:
            d *=0
    print('ДА' if d else 'НЕТ')
else:
    print('НЕТ')
