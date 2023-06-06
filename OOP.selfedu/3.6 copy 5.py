import sys

# здесь объявляйте класс
class BookStudy:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def __hash__(self):
        return hash((self.name.lower(),self.author))

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))  # список lst_in не менять!

# здесь продолжайте программу (используйте список строк lst_in)
lst_bs = []
for string in lst_in:
    lst_bs.append(BookStudy(*string.split(';')))

unique_books = 0
temp = set()
for book in lst_bs:
    temp.add(hash(book))

unique_books = len(temp)