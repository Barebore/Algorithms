def pig_it(text):
    from string import punctuation
    result = ''
    for char in text.split():
        if char not in punctuation:
            if '.' in char or ',' in char or '?' in char or '!' in char:
                result += char[1:len(char)-1] + char[0:1] + 'ay' + char[len(char)-1:] + (' ' if True else '')
            else:
                result += char[1:] + char[0:1] + 'ay '
        else:
            result += char

    return result[:len(result)]

print(pig_it('Pig latin, is cool?'))
print(pig_it('Quis custodiet ipsos custodes ?'))
print(pig_it('O tempora o mores !'))