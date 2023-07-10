class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job

    @classmethod
    def check_index(self, index):
        if index in [0, 1, 2, 3, 4]:
            return True
        raise IndexError('неверный индекс')


    def __getitem__(self, index):
        if self.check_index(index):
            return list(self.__dict__.values())[index]
    
    def __setitem__(self, index, value):
        if self.check_index(index):
            key = list(self.__dict__.keys())[index]
            self.__dict__[key] = value


    def __iter__(self):
        return iter(self.__dict__.values())
    
    # def __next__(self):
    #     return next(self.__dict__.values())

    
pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
print(pers[1])
pers[0] = 'Балакирев С.М.'
for v in pers:
    print(v)
# pers[5] = 123 # IndexError