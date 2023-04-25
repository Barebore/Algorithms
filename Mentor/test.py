def can_swap_letters(source: str, target: str) -> bool:
    counter = 0
    lst = []
    if len(source) != len(target):
        return False
    for i in range(len(source)):
        if source[i] != target[i]:
            lst.append(i)
    if len(lst) > 2 and len(lst) == 1:
        return False
    if len(lst) == 2:
        return set([source[lst[0]], source[lst[1]]]) == set([target[lst[0]], target[lst[1]]])
    if len(lst) == 0:
        return len(source) - len(set(str)) >= 1
