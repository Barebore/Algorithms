n = 3
list1 = [1, 2, 3]
list2 = [4, 5, 6]

n = 1
list1 = [1]
list2 = [2]

n = 4
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]

# n = int(input())
# list1 = list(map(int, input().split()))
# list2 = list(map(int, input().split()))
list3 = []
for i in range(2 * n):
	list3.append(list1.pop(0) if i % 2 == 0 else list2.pop(0))
                 
print(*list3)
        