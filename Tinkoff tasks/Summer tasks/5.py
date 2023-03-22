n = int(input())
a = list(map(int, input().split()))

max_ending_here = 0
max_so_far = {0: -1}
count = 0

for i in range(n):
    max_ending_here += a[i]
    if max_ending_here in max_so_far:
        if max_so_far[max_ending_here] + 1 <= i:
            count += max_so_far[max_ending_here] + 2
        else:
            count += 1
    max_so_far[max_ending_here] = i

print(count)