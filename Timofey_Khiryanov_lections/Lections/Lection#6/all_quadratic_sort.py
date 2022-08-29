def buble_sort(A):
    '''Сортировка списка А методом пузырька'''
    for x in range(1,len(A)):
        for k in range(len(A)-x):
            if A[k] > A[k+1]:
                A[k], A[k+1] = A[k+1], A[k]

def choise_sort_ascending(A):
    '''Сортировка списка А выбором по возрастанию'''
    for x in range(len(A)-1):
        for k in range(x+1,len(A),1):
            if A[x] > A[k]: # по возрастанию
                A[k], A[x] = A[x], A[k]

def choise_sort_descending(A):
    '''Сортировка списка А выбором по убыванию'''
    for x in range(len(A)-1):
        for k in range(x+1,len(A),1):
            if A[x] < A[k]: # по убыванию
                A[k], A[x] = A[x], A[k]

def insert_sort(A):
    '''Сортировка списка А вставками '''
    for x in range(1,len(A),1):
        for k in range(x,0,-1):
            if x > 0 and A[x] < A[k-1]:
                A[k-1], A[x] = A[x], A[k-1]
                x -= 1

def test_sort(sort_algorithm):
    print('testcase #1: ', end='')
    A = [4,2,5,1,3]
    A_sorted = [1,2,3,4,5]
    sort_algorithm(A)
    print('ok' if A == A_sorted else 'fail') #тернарный оператор
    
    print('testcase #2: ', end='')
    A = list(range(10,20)) + list(range(0,10))
    A_sorted = list(range(20))
    sort_algorithm(A)
    print('ok' if A == A_sorted else 'fail') #тернарный оператор

    print('testcase #3: ', end='')
    A = [4,2,2,1,4]
    A_sorted = [1,2,2,4,4]
    sort_algorithm(A)
    print('ok' if A == A_sorted else 'fail') #тернарный оператор

test_sort(insert_sort)
test_sort(choise_sort_ascending)
test_sort(buble_sort)