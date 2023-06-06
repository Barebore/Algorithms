import pprint
import sys


class DataBase:
    def __init__(self, path):
        self.path = path
        self.dict_db = {}

    def write(self, obj):
        if obj not in self.dict_db:
            self.dict_db[obj] = [obj]
        else:
            self.dict_db[obj].append(obj)


    def read(self, pk):
        for i in self.dict_db:
            if i.pk == pk:
                return i


class Record:
    pk = 0
    def __init__(self, fio, descr, old):
        self.fio = fio
        self.descr = descr
        self.old = int(old)
        # auto
        self.pk = Record.pk
        Record.pk += 1

    def __hash__(self):
        return hash((self.fio.lower(), self.old))
    
    def __eq__(self, other):
        if hash(self) == hash(other):
            return True
        else:
            return False
        

lst_in = list(map(str.strip, sys.stdin.readlines()))

# "ФИО; характеристика; возраст"
# Например:
# Балакирев С.М.; программист; 33
# Кузнецов А.В.; разведчик-нелегал; 35
# Суворов А.В.; полководец; 42
# Иванов И.И.; фигурант всех подобных списков; 26
# Балакирев С.М.; преподаватель; 37

db = DataBase("db.txt")

for i in lst_in:
    fio, descr, old = i.split(";")
    db.write(Record(fio, descr, old))

pprint.pprint(db.dict_db)
