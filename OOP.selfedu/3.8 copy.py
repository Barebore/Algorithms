class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
    
    def __getitem__(self, index):
        if not isinstance(index, int) or index < 0:
            raise IndexError('неверный индекс поля')
        try:
            field_name = list(self.__dict__.keys())[index]
            return self.__dict__[field_name]
        except IndexError:
            raise IndexError('неверный индекс поля')
    
    def __setitem__(self, index, value):
        if not isinstance(index, int) or index < 0:
            raise IndexError('неверный индекс поля')
        try:
            field_name = list(self.__dict__.keys())[index]
            self.__dict__[field_name] = value
        except IndexError:
            raise IndexError('неверный индекс поля')


    
r = Record(pk=1, title='Python ООП', author='Балакирев')
print(r.pk) # 1
print(r.title) # Python ООП
print(r.author) # Балакирев

r[0] = 2 # доступ к полю pk
r[1] = 'Супер курс по ООП' # доступ к полю title
r[2] = 'Балакирев С.М.' # доступ к полю author
print(r[1]) # Супер курс по ООП
print(r[2])
# r[3] # генерируется исключение IndexError
