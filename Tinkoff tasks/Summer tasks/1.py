a, b, c, d = map(int, input().split())

def check_stang_height(a, b, c, d):
    if  a >= b >=c >=d or a <= b <= c <= d:
        return 'YES'
    else:
        return 'NO'

print(check_stang_height(a,b,c,d))


# a, b, c, d = map(int, input()split())
# print('YES' if a >= b >=c >=d or a <= b <= c <= d else 'NO')
