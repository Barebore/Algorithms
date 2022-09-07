'''
Вася занимается строительством лесенок из блоков. Лесенка состоит из ступенек, при этом i-ая ступенька должна состоять ровно из i блоков.

По заданному числу блоков n определите максимальное количество ступенек в лесенке, которую можно построить из этих блоков.
'''

def calc_step(n):
    step = 0
    balance = n
    for i in range(1,n+1):
        if balance - i >= 0:
            step += 1
            balance = balance - i
        else:
            return step
    return step

n = int(input())
print(calc_step(n))