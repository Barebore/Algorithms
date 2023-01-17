import string
verify_symbol = string.ascii_lowercase[:13]

def printer_error(s):
    result = 0
    for symb in s:
        if symb not in verify_symbol:
            result += 1
    answer = f'{result}/{len(s)}'
    return answer



print(printer_error('aaabbbbhaijjjm'))
print(printer_error('aaaxbbbbyyhwawiwjjjwwm'))
