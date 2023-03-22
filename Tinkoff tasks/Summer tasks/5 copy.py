def foo(length, lst):
    count = 0
    for i in range(length-1):
        for j in range(i+1, length):
            if sum(lst[i:j+1]) == 0:
                count += length - j
                break
    return count


length = int(input())
lst = list(map(int, input().split()))
print(foo(length, lst))

# print(foo(3, [42, -42, 42]))
# print(foo(4, [1, 2, 3, -6]))
# print(foo(5, [-1, 1, 2, -3, 6]))