n = int(input())
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
list3 = [x for pair in zip(list1, list2) for x in pair]
print(*list3)