# put your python code here
n = int(input())
anton = ['a','n','t','o','n']
lst = [input() for i in range(n)]
for freez in lst:
    if ('a' in freez and
    'n' in freez[freez.find('a')+1:] and
    't' in freez[freez.find('n')+1:] and
    'o' in freez[freez.find('t')+1:] and
    'n' in freez[freez.find('o')+1:]):
        print(lst.index(freez)+1, end = ' ')
#print(lst)

# put your python code here
n = int(input())
anton = ['a','n','t','o','n']
lst = [input() for i in range(n)]
for freez in lst:
    if 'a' in freez:
        freez = freez[freez.find('a')+1:]
        print(1123,freez)
#print(lst)
