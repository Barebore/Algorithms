n = int(input())
arr = list(map(int, input().split()))

min_index = arr.index(min(arr))
max_index = arr.index(max(arr))

print(min_index+1, max_index+1)