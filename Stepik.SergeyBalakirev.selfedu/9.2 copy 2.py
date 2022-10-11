# put your python code here

def get_simple_numbers():
    for x in range(2,10000):
        bl = 1
        for i in range(2,x):
            if x % i == 0:
                bl = 0
        if bl:
            yield x
       

    
n = 20
s = get_simple_numbers()
for i in range(20):
    print(next(s), end = ' ')
