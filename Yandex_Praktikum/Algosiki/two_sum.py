def two_sum(n, lst, value):
    for i in range(n):
        for j in range(i+1, n):
            if lst[i] + lst[j] == value:
                return lst[i], lst[j]
    return (None,)


n = int(input())
lst = list(map(int, input().split()))
value = int(input())

print(two_sum(n, lst, value))

# assert two_sum(6, [-1, -1, -9, -7, 3 ,-6], 2) == (-1, ), 'failed1'
# assert two_sum(8, [6, 2, 8, -3, 1, 1, 6, 10], 100) == None, 'failed2'