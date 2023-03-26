n = int(input())
arr = list(map(int, input().split()))

print(arr.index(max(arr)) + 1, arr.index(min(arr)) + 1)