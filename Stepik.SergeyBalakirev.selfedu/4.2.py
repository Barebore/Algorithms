month, day = map(int, input().split())
mda =  [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
d1,d2 = 0,0
m1,m2 = 0,0
if day == 1:
    d1 = mda[month-1]
    m1 = month-1
    d2 = day + 1
    m2 = month
elif day == mda[month-1]:
    d1 = day - 1
    m1 = month
    d2 = 1
    m2 = month + 1
else:
    d1 = day - 1
    m1 = month
    d2 = day + 1
    m2 = month
print(f'{(str(m1).rjust(2, "0"))}.{str(d1).rjust(2, "0")} {(str(m2).rjust(2, "0"))}.{str(d2).rjust(2, "0")}')
