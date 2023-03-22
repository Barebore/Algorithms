def height_check(h1, h2, h3, h4):
    if h1 >= h2 >= h3 >= h4 or h1 <= h2 <= h3 <= h4:
        return 'YES'
    else:
        return 'NO'


h1, h2, h3, h4 = map(int, input().split())
print(height_check(h1, h2, h3, h4))
