from string import ascii_lowercase, digits
import random as rd

class EmailValidator:

    __CHARS = ascii_lowercase
    __CHARS_CORRECT = __CHARS + __CHARS.upper() + digits + '_.'

    def __new__(self):
        return None

    @classmethod
    def get_random_email(cls):
        email = ''
        l = len(cls.__CHARS_CORRECT)
        for i in range(rd.randint(0,99)):
            email += cls.__CHARS_CORRECT[rd.randint(0,l-1)]
        return email+'@gmail.com'
    
    @classmethod
    def check_email(cls, email):
        if cls.__is_email_str(email):
            if '@' in email:
                if email.count('@') == 1:
                    if len(email.split('@')[0]) <= 100:
                        if len(email.split('@')[1]) <= 50:
                            if '.' in email.split('@')[1]:
                                if '..' not in email.split('@')[1] and '..' not in email.split('@')[0]:
                                    for i in email.split('@')[0]:
                                        if i not in cls.__CHARS_CORRECT:
                                            return False
                                    for i in email.split('@')[1]:
                                        if i not in cls.__CHARS_CORRECT:
                                            return False        
                                    return True    
        return False

    @staticmethod
    def __is_email_str(email):
        if type(email) == str:
            return True
        return False

assert EmailValidator.check_email("sc_lib@list.ru") == True and EmailValidator.check_email("sc_lib@list_ru") == False and EmailValidator.check_email("sc@lib@list_ru") == False and EmailValidator.check_email("sc.lib@list_ru") == False and EmailValidator.check_email("sclib@list.ru") == True and EmailValidator.check_email("sc.lib@listru") == False and EmailValidator.check_email("sc..lib@list.ru") == False, "метод check_email отработал некорректно"
m = EmailValidator.get_random_email()
assert EmailValidator.check_email(m) == True, "метод check_email забраковал сгенерированный email методом get_random_email"
assert EmailValidator() is None, "при создании объекта класса EmailValidator возвратилось значение отличное от None"
assert EmailValidator._EmailValidator__is_email_str('abc'), "метод __is_email_str() вернул False для строки"
 