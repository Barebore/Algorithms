def find(number,A):
    '''ищет х в А и вовзращает True, если такой есть
        False, если такого нет
    '''
    for x in A:
        if number == x:
            return True
    return False

def generate_permutations(N:int, M:int=-1, prefix = None):
    ''' Генерация всех перестановок N чисел в М позициях,
        с префиксом prefix
    '''
    M = N if M == -1 else M # по умолчанию N чисел в N позициях
    prefix = prefix or [prefix]
    if M == 0:
        print(prefix)
        return
    for number in range(1,N+1):
        if find(number,prefix): 
            continue
        prefix.append(number)
        generate_permutations(N, M-1, prefix)
        prefix.pop


generate_permutations(3)