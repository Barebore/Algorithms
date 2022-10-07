# put your python code here

#f = 0.5 * pow(x, 2) - 2.0
a,b = map(int, input().split())
gen = ((0.5 * pow(x, 2) - 2.0) for x in range(a,b+1,0.01))

for i in range(20):
    print(next(gen), end = ' ')
