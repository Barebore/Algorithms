n = int(input())
dice = []
for i in range(n):
    dice.append(list(map(int, input().split())))
sums = set()
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            for a in dice[i]:
                for b in dice[j]:
                    for c in dice[k]:
                        sums.add(a+b+c)
print(len(sums))