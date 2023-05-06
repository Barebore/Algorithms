def binarySearch(arr, cost, left, right):
    if cost > arr[-1]:
        return -1
    if right <= left: # промежуток пуст
        return right +1
    # промежуток не пуст
    mid = (left + right) // 2
    if arr[mid] == cost or cost < arr[mid]: # центральный элемент — искомый
        return binarySearch(arr, cost, left, mid)
    else: # иначе следует искать в правой половине
        return binarySearch(arr, cost, mid + 1, right)


cout_day = int(input())
arr = list(map(int, input().split()))
cost_bicycle = int(input())

print(binarySearch(arr, cost_bicycle, left = 0, right = len(arr)), end=' ')
print(binarySearch(arr, cost_bicycle*2, left = 0, right = len(arr)))