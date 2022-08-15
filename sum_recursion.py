def sum(arr):
    if arr == []:
        return 0
    print(arr[1:])
    return arr[0] + sum(arr[1:])


A = list(range(5))
#A = [1,2]
#print(A.pop(0))
#print(A)
print(sum(A))