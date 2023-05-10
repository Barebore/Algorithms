lst = ['1', '3', '3', '19', '18', '199', '182']

def special_comparator(value1, value2):
    while value1 != '' and value2 != '':
        if int(value1[0]) > int(value2[0]):
            return True
        elif int(value1[0]) == int(value2[0]):
            value1 = value1[1:]
            value2 = value2[1:]
            continue
        else:
            return False
    if value1 == '0' and value2 == '':
        return False
    if value2 == '0' and value1 == '':
        return True
    value1 += '0'*(max(1-len(value1), 0))
    value2 += '0'*(max(1-len(value2), 0))
    if int(value1) // 10**(len(value1)-1) == 9:
        return True
    if int(value2) // 10**(len(value2)-1) == 9:
        return False
    if int(value2) == 0:
        return False
    if int(value1) == 0:
        return False
    return True

def special_sort(array, less):
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i
        # заменим сравнение item_to_insert < array[j-1] на компаратор less
        while j > 0 and less(item_to_insert, array[j-1]):
            array[j] = array[j-1]
            j -= 1
            array[j] = item_to_insert


# print(special_comparator('1','199'))
lst = ['4', '1', '19', '18', '199', '182', '191']
n = int(input())
lst = input().split()

special_sort(lst, special_comparator)
print(lst)
print(''.join(lst))