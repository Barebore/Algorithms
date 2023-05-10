n = int(input())
lst = list(map(int, input().split()))

print(''.join(map(str, sorted(lst, key=lambda x: x // 10**(len(str(x))-1), reverse=True))))
