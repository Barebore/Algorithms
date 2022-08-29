A = [4,2,5,1,3]
def choise_sort_ascending(A):
    '''Сортировка списка А выбором по возрастанию'''
    for x in range(len(A)-1):
        for k in range(x+1,len(A),1):
            if A[x] > A[k]: # по возрастанию
                A[k], A[x] = A[x], A[k]
choise_sort_ascending(A)
print(A)

A = [4,2,5,1,3]
def choise_sort_descending(A):
    '''Сортировка списка А выбором по убыванию'''
    for x in range(len(A)-1):
        for k in range(x,len(A),1):
            if A[x] < A[k]: # по убыванию
                A[k], A[x] = A[x], A[k]
choise_sort_descending(A)
print(A)