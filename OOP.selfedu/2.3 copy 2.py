class ValidateString:
    def __init__(self, min_length = 3, max_length = 100):
        self.min_lenght = min_length
        self.max_length = max_length

    def validate(self, string):
        if type(string) == str and self.max_length >= len(string) >= self.min_lenght:
            return True
        return False

class StringValue:

    def __init__(self, validator):
        self.validator = validator

    def __set_name__(self, owner, name):
        self.name = '_'+name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.validator.validate(value):
            setattr(instance, self.name, value)

class RegisterForm:
    login = StringValue(validator = ValidateString())
    password = StringValue(validator = ValidateString())
    email = StringValue(validator = ValidateString())

    def __init__(self, login, password, email):
        self.login = login
        self.password = password
        self.email = email
    
    def get_fields(self):
        a = []
        a.append(self.login)
        a.append(self.password)
        a.append(self.email)
        return a

    def show(self):
        print('<form>')
        print(f'Логин:{self.login}')
        print(f'Пароль:{self.password}')
        print(f'Email:{self.email}')
        print('<form>')

assert hasattr(ValidateString, 'validate'), "в классе ValidateString отсутствует метод validate"
r = RegisterForm('11111', '1111111', '11111111')
assert hasattr(r,'login') and hasattr(r, 'password') and hasattr(r, 'email'), "в классе RegisterForm должны быть дескрипторы login, password, email"
assert hasattr(RegisterForm, 'show'), "в классе RegisterForm отсутствует метод show"
StringValue.__doc__
frm = RegisterForm("123", "2345", "sc_lib@list.ru")
assert frm.get_fields() == ["123", "2345", "sc_lib@list.ru"], "метод get_fields вернул неверные данные"
frm.login = "root"
assert frm.login == "root", "дескриптор login вернул неверные данные"
v = ValidateString(5, 10)
assert v.validate("hello"), "метод validate вернул неверное значение"
assert v.validate("hell") == False, "метод validate вернул неверное значение"
assert v.validate("hello world!") == False, "метод validate вернул неверное значение"

class A:
    st = StringValue(validator=ValidateString(3, 10))

a = A()
a.st = "hello"
assert a.st == "hello", "дескриптор StringValue вернул неверное значение"
a.st = "d"

assert a.st == "hello", "дескриптор StringValue сохранил строку длиной меньше min_length"
a.st = "dапарпаропропропропр"
assert a.st == "hello", "дескриптор StringValue сохранил строку длиной больше max_length"
a.st = "dапарпароп"
assert a.st == "dапарпароп", "дескриптор StringValue сохранил строку длиной больше max_length"