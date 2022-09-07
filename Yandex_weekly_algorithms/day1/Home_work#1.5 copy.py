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

    bool = 0
    count = 1

    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            count += 1
        else:
            bool = 0  

    if count == len(string):
        bool = 1

    if bool == 1:
        if string[len(string)-1] == 'a':
            string.pop(len(string)-1)
            return string
        else:
            for i in range(len(alphabet)):
                if string[len(string)-1] == alphabet[i]:
                    string[len(string)-1] = alphabet[i-1]
        return string

    if len(string) == 3:
        if string[-1] == 'a':
            string.pop(len(string)-1)
            return string
        else:
            for i in range(len(alphabet)):
                if string[-1] == alphabet[i]:
                    string[-1] = alphabet[i-1]
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

# b = ''.join(map(str,string))
# a = ''.join(map(str,lol(string)))
# if a < b:
#     print(a,'<',b)
#     print('successful')
print(''.join(map(str,lol(string))))
# print('successful3' if 'abba' > 'abaa' else 'error')
print('ok' if 'aaba' < 'abaa' else 'not ok')