def number_of_options(course_list, balance_list):
    answer = 1
    # для удобства разнесём значения по переменным
    a_price = course_list[0]
    b_price = course_list[1]
    c_price = course_list[2]
    a_balance = balance_list[0]
    b_balance = balance_list[1]
    c_balance = balance_list[2]
    # переведём все валюты в валюту С
    cash = a_balance / a_price
    a_balance -= cash * a_price
    c_balance += cash * c_price
    cash = b_balance / b_price
    b_balance -= cash * b_price
    c_balance += cash * c_price
    #Перебор всех возможных значений
    while (b_balance >= b_price or c_balance >= c_price):
        while (c_balance >= c_price): # меняем c на b
            c_balance -= c_price
            b_balance += b_price
            answer += 1
        if (b_balance >= b_price): # можно ли обменять b
            b_balance -= b_price; # меняем a на b
            a_balance += a_price
            answer += 1
        while (b_balance >= b_price): # меняем b на c
            b_balance -= b_price
            c_balance += c_price
            answer += 1
        if (c_balance >= c_price): # можно ли обменять c
            c_balance -= c_price # меняем a на c
            a_balance += a_price
            answer += 1
    return answer

course_list = list(map(int, input().split()))
balance_list = list(map(int, input().split()))
print(number_of_options(course_list, balance_list))