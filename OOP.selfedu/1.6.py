# здесь объявляйте класс SingletonFive
class SingletonFive:
    cout = 0
    def __new__(cls, *args, **kwargs):
        __instance = None
        if cls.cout <= 4:
            cls.__instance = super().__new__(cls)
            cls.cout += 1
            # print('   ',cls.cout)
        return cls.__instance
    
    def __init__(self, name):
        self.name = name

objs = [SingletonFive(str(n)) for n in range(10)] # эту строчку не менять
# for i in objs:
#     print(i.name)