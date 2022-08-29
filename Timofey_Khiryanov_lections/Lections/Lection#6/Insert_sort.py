A = [4,2,5,1,3]
def insert_sort(A):
    '''Сортировка списка А вставками '''
    for x in range(1,len(A),1):
        print('первый цикл № x=', x)
        for k in range(x,0,-1):
            print('k =',k,'сравниваемые элементы', A[x], A[k-1])
            if A[x] < A[k-1]:
                print('прошло')
                A[k-1], A[x] = A[x], A[k-1]
                x -= 1
                print(A)
insert_sort(A)
print(A)

