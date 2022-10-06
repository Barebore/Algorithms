import time

def test_time(func):
    def wraper(*args, **kwargs):
        st = time.time()
        result = func(*args, **kwargs)
        et = time.time()
        dt = et - st
        print(f"time: {dt} sek")
        return result

    return wraper


@test_time
def get_nod_fast(a, b):
    while b > 0: a, b = b, a % b
    return a


@test_time
def get_nod_slow(a, b):
    while a != b:
        if a > b: a -= b
        else: b -= a
    return a

    
#get_nod_slow = test_time(get_nod_slow)
#get_nod_fast = test_time(get_nod_fast)

res1 = get_nod_slow(2, 100000000)
res2 = get_nod_fast(2, 100000000)
print(res1, res2)