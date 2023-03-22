def foo(length, lst):
    count = 0
    prefix_sums = [0] * (length + 1)
    for i in range(1, length + 1):
        prefix_sums[i] = prefix_sums[i-1] + lst[i-1]    
    for i in range(length-1):
        for j in range(i+1, length+1):
            if prefix_sums[j] - prefix_sums[i] == 0:
                count += length - j + 1
                break
    return count


length = int(input())
lst = list(map(int, input().split()))
print(foo(length, lst))

# print(foo(3, [42, -42, 42]))
# print(foo(4, [1, 2, 3, -6]))
# print(foo(5, [-1, 1, 2, -3, 6]))
