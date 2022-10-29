TYPE_OS = 1 # 1 - Windows; 2 - Linux

class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"

class Dialog:
    def __new__(cls, *args, **kwargs):
        if TYPE_OS == 1:
            obj = super().__new__(DialogWindows)
            setattr(obj, 'name', args[0])
            return obj
        obj = super().__new__(DialogLinux)
        setattr(obj, 'name', args[0])
        return obj

# здесь объявляйте класс Dialog

TYPE_OS = 1
dlg_1 = Dialog("123")
TYPE_OS = 2
dlg_2 = Dialog("1234")
print(dlg_1.name, dlg_2.name)

d1 = Dialog("12")
d2 = Dialog("123")
print(d1.name, d2.name)
print(dlg_2.name)
print(d1.name)
print(d2.name)