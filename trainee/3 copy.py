n, k = map(int, input().split())
arr = list(map(int, input().split()))

pointer = 0
counter = 0
for i in range(1, len(arr)+1):
    if sum(arr[pointer:i]) <= k and arr[pointer:i].count(0) <= 1:
        counter += len(arr[pointer:i])
    else:
        while pointer+1 != i:
            pointer += 1
            if sum(arr[pointer:i]) <= k and arr[pointer:i].count(0) <= 1:
                counter += 1
print(counter)
