import random

def find_smallest_sum(arr):
    min_1 = float('inf')
    min_2 = float('inf')
    for i in arr:
        if i < min_1 or i < min_2:
            if i < min_1 and i < min_2:
                min_2 = min_1
                min_1 = i
                continue
            if i < min_2:
                min_2 = i
    return min_1,min_2

arr = [1, 3, 7, 4, 2, 9, 8]
print(find_smallest_sum(arr))

for i in range(99999):
    lst = []
    for i in range(500):
        lst.append(random.randint(-200, 200))
    print(lst)
    if find_smallest_sum(lst) != (lst.pop(lst.index(min(lst))), lst.pop(lst.index(min(lst)))):
        print(find_smallest_sum(lst))
        print((lst.pop(lst.index(min(lst))), lst.pop(lst.index(min(lst)))))
        raise ValueError()
    else:
        print(True)
