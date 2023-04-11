length = int(input())
lst = list(input().split())
length_word = 0
word = ''
for value in lst:
    if length_word < len(value):
        length_word = len(value)
        word = value
print(word)
print(length_word)
# print(max(list(map(len, input().split()))))