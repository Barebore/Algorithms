def merge(arr, left, mid, right):
    n1 = mid - left
    n2 = right - mid
    left_arr = arr[left:left+n1]
    right_arr = arr[mid:mid+n2]
    left_arr.append(float('inf'))
    right_arr.append(float('inf'))
    i = j = 0
    for k in range(left, right):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
    return arr[left:right]

def merge_sort(arr, left, right):
    if right - left > 1:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid, right)
        merge(arr, left, mid, right)