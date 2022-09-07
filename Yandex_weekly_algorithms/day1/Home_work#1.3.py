'''
У вас есть 1000$, которую вы планируете эффективно вложить. Вам даны цены за 1000 кубометров газа за n дней. Можно один раз купить газ на все деньги в день i и продать его в один из последующих дней j, i < j.

Определите номера дней для покупки и продажи газа для получения максимальной прибыли.

Формат ввода
В первой строке вводится число дней n (1 ≤ n ≤ 100000).

Во второй строке вводится n чисел — цены за 1000 кубометров газа в каждый из дней. Цена — целое число от 1 до 5000. Дни нумеруются с единицы.

Формат вывода
Выведите два числа i и j — номера дней для покупки и продажи газа. Если прибыль получить невозможно, выведите два нуля.'''

def number_profit_day(day,price):
    print('')
    profit = 0
    day1 = 0
    day2 = 1
    for i in range(day-1):
        print(day1,day2,'if', price[day2],'-' ,price[i],'>',profit)
        if price[day2] - price[i] > profit:
            profit = price[day2] - price[i]
            day1 = i
            day2 = i+1
        else:
            day2 +=1
    print(day1+1,day2+1)
    return day1+1,day2+1



def test_number_profit_day():
    print('testcase #1: ', end='')
    day = 6
    price = [9,8,7,1,2,3]
    x,y = 4,6
    a,b = number_profit_day(day,price)
    print('ok' if a == x and b == y else 'fail')
    # print('testcase #2: ', end='')
    # day = 6
    # price = [10,3,5,3,11,9]
    # x,y = 2,5
    # a,b = number_profit_day(day,price)
    # print('ok' if a == x and b == y else 'fail')
    # print(a,b)

    # print('testcase #3: ', end='')
    # day = 6
    # price = [10,3,5,2,3,3]
    # x,y = 2,3
    # a,b = number_profit_day(day,price)
    # print('ok' if a == x and b == y else 'fail')
    # print(a,b)

    # print('testcase #4: ', end='')
    # day = 6
    # price = [10,3,6,2,3,6]
    # x,y = 4,6
    # a,b = number_profit_day(day,price)
    # print('ok' if a == x and b == y else 'fail')
    # print(a,b)


#day = int(input()) # количество дней
#price = list(map(int, input().split()))
test_number_profit_day()
#print(number_profit_day(day,price))