def chunked():
    pass

a = input().replace(' ','')
n = int(input())
lst = []
lst_temp = []
i = 0
for x in a:
    if i != n:
        lst_temp.append(x)
        i += 1
    else:
        i = 1
        lst.append(lst_temp)
        lst_temp = []
        lst_temp.append(x)
lst.append(lst_temp)

print(lst)