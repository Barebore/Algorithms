from string import ascii_lowercase, digits

class LoginForm:
    def __init__(self, name, validators=None):
        self.name = name
        self.validators = validators
        self.login = ""
        self.password = ""
        
    def post(self, request):
        self.login = request.get('login', "")
        self.password = request.get('password', "")
        
    def is_validate(self):
        if not self.validators:
            return True
        
        for v in self.validators:
            if not v(self.login) or not v(self.password):
                return False
            
        return True

class LengthValidator:
    
    def __init__(self, min_lenght: int, max_lenght: int):
        self.min_lenght = min_lenght
        self.max_lenght = max_lenght

    
    def __call__(self, *args, **kwargs):
        return self.min_lenght <= len(args[0]) <= self.max_lenght

class CharsValidator:

    def __init__(self, chars):
        self.chars = chars

    def __call__(self, *args, **kwargs):
        return set(args[0]) <= set(self.chars)

cv = CharsValidator(ascii_lowercase + digits)
res = cv('panda')
print(res)
print(res)
lg = LoginForm("Вход на сайт", validators=[LengthValidator(3, 50), CharsValidator(ascii_lowercase + digits)])
lg.post({"login": "root", "password": "panda"})
if lg.is_validate():
    print("Дальнейшая обработка данных формы")
