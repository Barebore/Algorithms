def moving_average(n, lst, width):
    result = []
    current_sum = sum(lst[0:width])
    result.append(current_sum / width)
    for i in range(0, n - width):
        current_sum -= lst[i]
        current_sum += lst[i + width]
        current_avg = current_sum / width
        result.append(current_avg)
    return result


n = int(input())
lst = list(map(int, input().split()))
k = int(input())

print(*moving_average(n, lst, k))