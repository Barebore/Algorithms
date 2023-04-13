a = input()
b = input()
if  len(b) > len(a):
    a, b = b, a
a = a[::-1]
b = b[::-1]
flag = 0
result = []


for i, symb in enumerate(a):
    if len(b) <= i:
        if flag == 1:
            if symb == '1':
                for j, symb2 in enumerate(a[i:]):
                    if flag == 1 and symb2 == '1':
                        result.append('0')
                    elif symb2 == '0' and flag == 1:
                        result.append('0')
                    else:
                        result.append(symb2)
            else:
                result.append('1')
                result.append(a[i+1:])
            flag = 0
        else:
            result.append(a[i:])
        break
    if symb == '1' and b[int(i)] == '1' and flag == 1:
        result.append('1')
        flag = 1
        continue
    if (symb == '1' or b[int(i)] == '1') and flag == 1:
        result.append('0')
        flag = 1
        continue
    if symb == '1' and b[int(i)] == '1':
        result.append('0')
        flag = 1
        continue
    if symb == '1' or b[int(i)] == '1':
        result.append('1')
        flag = 0
        continue
    if flag == 1:
        result.append('1')
        flag = 0
        continue
    result.append('0')
if flag == 1:
    result.append('1')
print((''.join(result))[::-1])