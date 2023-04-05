n, k = map(int, input().split())
arr = list(map(int, input().split()))

pointer = 0
counter = 0
for i in range(1, len(arr)+1):
    # print(arr[pointer:i])
    # print(sum(arr[pointer:i]), arr[pointer:i].count(0))
    if sum(arr[pointer:i]) <= k and arr[pointer:i].count(0) <= 1:
        counter += len(arr[pointer:i])
        # print(counter, 'YES')
    else:
        # print('NO')
        while pointer+1 != i:
            pointer += 1
            # print(arr[pointer:i])
            # print(sum(arr[pointer:i]), arr[pointer:i].count(0))
            if sum(arr[pointer:i]) <= k and arr[pointer:i].count(0) <= 1:
                counter += 1
                # print(counter, 'YES')
            # else:
            #     print('NO')

        # if arr[i-1] <= k:
        #     counter += 1
        #     print(arr[i-1], 'меньше К')
        # pointer = i-1
        # print(pointer,'NO')

print(counter)
