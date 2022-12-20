# public static uint highestOneBit(uint i) 
# {
#     i |= (i >>  1);
#     i |= (i >>  2);
#     i |= (i >>  4);
#     i |= (i >>  8);
#     i |= (i >>  16);
#     return i - (i >> 1);
# }
from math import log

def highest_one_bit(i):
    i |= (i >>  1)
    i |= (i >>  2)
    i |= (i >>  4)
    i |= (i >>  8)
    i |= (i >>  16)
    return i - (i >> 1)

def high_bit_order(n):
    k = int(log(n, 2))
    if k:
        x = n >> (k-1)
        if x == 1: # correct log() imprecision for very large integers
            return k - 1
        elif 2 <= x < 4:
            return k
        else: # very unlikely, but handled
            raise ValueError("high_bit_order() failed on unusual value.")
    else:
        return k

def task6(n):
    number_set = set()
    max_result = 0
    max_value = 0
    max_flag = False

    def search_and_add(current):
        max_result = 0
        if number_set == {}:
            print('ololo')
            return 0
        for i in number_set:
            first = i
            result = first ^ current
            if result > max_result:
                max_result = result
        number_set.add(current)
        return max_result
        

    for _ in range(n):
        current = int(input())
        # number_set.append(current)
        if not max_flag:
            result = search_and_add(current)
            if (result > max_result):
                max_result = result
                max_value = highest_one_bit(max_result) * 2 - 1
        else:
            if current > max_value:
                max_flag = False
                result = search_and_add(current)
                if result > max_result:
                    max_result = result
                    max_value = highest_one_bit(max_result) * 2 - 1
        if result == max_value:
            max_flag = True
        print(max_result, number_set)
n = int(input())
task6(n)