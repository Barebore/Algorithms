# put your python code here
len_lst = int(input())
lst = [int(input()) for i in range(len_lst)]
number = int(input())
flag = False
for i in lst:
    for j in lst:
        # print(i*j)
        # if i == j:
        #     continue
        if i*j == number:
            # print(i*j)
            flag = True
            
print('ДА' if flag else 'НЕТ')



