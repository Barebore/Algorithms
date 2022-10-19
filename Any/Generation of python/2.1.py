# put your python code here
x = '123'
y = ''
for i in range(-1,-len(x),-1):
    print(i, x[i])
    if i % 3 == 0:
        y += x[i] + ','
        print('srabotalo')
    else:
        y += x[i]
print(x[0]+y[::-1])
