# char_amount = int(input())
# departaments = input()
# colors_char = input()

departaments = input()
colors_char = input()
def cout_ugly_words(departaments, colors_char):
    departaments_list = list(departaments.split()) # даелам список слов
    color_index = 0 # индекс символа в строке с цветами
    ugly_words = 0 #счётчик некрасивых слов
    for word in departaments_list: # для каждого слова в списке слов
        flag = 0 
        for _ in range(len(word)-1): # цикл от 0 до длины_слова - 1
            current_char = colors_char[color_index]
            next_char = colors_char[color_index + 1]
            if current_char == next_char: 
                flag = 1
            color_index +=1
        color_index +=1
        ugly_words += flag
    return ugly_words

print(cout_ugly_words(departaments, colors_char))

assert cout_ugly_words('Tinkoff', 'BYBYBYB') == 0, 'Fail'
#print(cout_ugly_words('Tinkoff', 'BYBYBYB00'))
assert cout_ugly_words('Algorithms and Data Structures', 'BBBBBBBBBBBYBYYYYBBBBBBBBBB') == 3, 'Fail'
#print(cout_ugly_words('Algorithms and Data Structures', 'BBBBBBBBBBBYBYYYYBBBBBBBBBB'))
assert cout_ugly_words('Tinkoff', 'BBBBBBB') == 1, 'Fail'
assert cout_ugly_words('Prostoslovo', 'BYBYBYBYBYY') == 1, 'Fail'
assert cout_ugly_words('Tinkoff', 'BYBYBYB') == 0, 'Fail'