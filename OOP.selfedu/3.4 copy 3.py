class Lib:
    def __init__(self):
        self.book_list = []

    def __add__(self, other):
        self.book_list.append(other)
        return self

    def __iadd__(self, other):
        self = self + other
        return self
    
    def __sub__(self, other):
        if isinstance(other, Book):
            del(self.book_list[self.book_list.index(other)])
        else:
            del(self.book_list[other])
        return self
    
    def __isub__(self, other):
        self = self - other
        return self
    
    def __len__(self):
        return len(self.book_list)
    
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    