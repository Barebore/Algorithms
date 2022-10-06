# put your python code here
def counter_add(n):
    def counter_add_n(x):
        return x+n
    return counter_add_n

k = int(input())

cnt = counter_add(2)
print(cnt(k))



