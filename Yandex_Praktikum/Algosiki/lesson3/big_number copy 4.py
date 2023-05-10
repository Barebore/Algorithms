lst = ['1', '3', '3', '19', '18', '199', '182']

def special_comparator(value1, value2):
    if int(value1 + value2) > int(value2 + value1):
        return True
    else:
        return False

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