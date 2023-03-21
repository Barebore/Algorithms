from collections import Counter

def foo(n, lst):
    for i in range(n, 2, -1):
        counts = Counter(lst[0:i])
        max1, min1 = counts.most_common(1)[0][1], counts.most_common()[-1][1]
        countmax, countmin = counts.values().count(max1), counts.values().count(min1)
        if max1 - min1 == 1 and (countmax == 1 or countmin == 1):
            return i
        if max1 == min1:
            return i

n = int(input())
lst = list(map(int, input().split()))
print(foo(n, lst))


# n = 13
# a = [1, 2, 3, 1, 2, 2, 3, 3, 3, 1, 4, 4, 5]
# print(foo(n, a))
# n = 10
# a = [1, 2, 4, 2, 3, 1, 3, 9, 15, 23]
# print(foo(n, a))
# n = 5
# a = [1, 2, 3, 4, 5]
# print(foo(n, a))

        



# from collections import defaultdict


# a = [1,1,1,2,3,4]
# counts = defaultdict(int)
# for x in a:
#     counts[x] += 1

# from collections import defaultdict

# def foo(n, lst):
#     for i in range(n, 2, -1):
#         counts = {}
#         counts = defaultdict(int)
#         for x in lst[0:i]:
#             counts[x] += 1
#             # print(x, counts)
#         # print(i)
#         max1 = max(counts.values())
#         min1 = min(counts.values())
#         countmax = [value for key, value in counts.items()].count(max1)
#         countmin = [value for key, value in counts.items()].count(min1)
#         # print(max1, min1, countmax, countmin)
#         if max1 - min1 == 1 and (countmax == 1 or countmin == 1):
#             print(counts)
#             return i
#         if max1 == min1:
#             print(counts)
#             return i
# n = int(input())
# lst = list(map(int, input().split()))
# print(foo(n, lst))