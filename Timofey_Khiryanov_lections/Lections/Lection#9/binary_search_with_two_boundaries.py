def left_bound(A, key):
    '''Функция, которая ищет левую границу искомого числа'''
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (left+right)//2
        if A[middle] < key:
            left = middle
        else:
            right = middle
    return left

def right_bound(A,key):
    '''Функция, которая ищет правую границу искомого числа'''
    left = -1
    right = len(A)
    while right-left > 1:
        middle = (left+right)//2
        if A[middle] <= key:
            left = middle
        else:
            right = middle
    return right

def print_search_numbers(A,key):
    i = left_bound(A,key)+1
    while i < right_bound(A,key):
        print(A[i])
        i += 1
A = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,6,6,6,6,6,7,7,8]

print_search_numbers(A,1)
