n = int(input())
lst = list(map(int, input().split()))
max = float('-inf')
min = float('inf')
min_index = 0
max_index = 0

for i, value in enumerate(lst):
    if  value >= max:
        max = value
        max_index = i
    if value < min:
        min = value
        min_index = i

print(max_index+1, min_index+1)