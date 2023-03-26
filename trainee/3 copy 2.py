n, k = map(int, input().split())
arr = list(map(int, input().split()))

pointer = 0
counter = 0

for i in range(1, len(arr) + 1):
    sub_arr = arr[pointer:i]
    if sum(sub_arr) <= k and sub_arr.count(0) <= 1:
        counter += len(sub_arr)
    else:
        while pointer + 1 != i:
            pointer += 1
            sub_arr = arr[pointer:i]
            if sum(sub_arr) <= k and sub_arr.count(0) <= 1:
                counter += 1

print(counter)