string = list(map(str, input()))
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def lol(string):
    if string == '':
        return ''
    if len(string) == 1:
        if string[0] == 'a':
            return ''
        else:
            for i in range(len(alphabet)):
                if string[0] == alphabet[i]:
                    string[0] = alphabet[i-1]
            return string
    if len(string) % 2 == 0:
        number_middle_symbol = len(string)//2-1
        for i in range(len(alphabet)):
            if string[number_middle_symbol] == alphabet[i]:
                string[number_middle_symbol] = alphabet[i-1]
    if len(string) % 2 == 1:
        number_middle_symbol = len(string)//2-1
        for i in range(len(alphabet)):
            if string[number_middle_symbol] == alphabet[i]:
                string[number_middle_symbol] = alphabet[i-1]
    return string


print(''.join(map(str,lol(string))))
