def move_zeros(lst):
    for i, number in enumerate(lst):
        if number == 0:
            del lst[i]
            lst.append(0)
    return lst


print(move_zeros([0, 3, 0, 0, 5, 0, 5, 2, 3, 0]))


def move_zeros1(lst):
    temp = [i for i in lst if i != 0]
    for i in range(lst.count(0)):
        temp.append(0)
    return temp


print(move_zeros1([0, 3, 0, 0, 5, 0, 5, 2, 3, 0]))