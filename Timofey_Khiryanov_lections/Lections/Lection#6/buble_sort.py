A = [4,2,5,1,3]
def buble_sort(A):
    '''Сортировка списка А методом пузырька'''
    for x in range(1,len(A)):
        print('cycle #',x)
        for k in range(len(A)-x):
            print('cycle # k =',k)
            if A[k] > A[k+1]:
                A[k], A[k+1] = A[k+1], A[k]

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
    

buble_sort(A)
print(A)