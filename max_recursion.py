def max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max(list[1:])
    return list[0] if list[0] > sub_max else sub_max

A = [4,6,1,70,4,0,32,5,2,4]
print(max(A))
B = list(range(100))
print(max(B))