from string import ascii_lowercase, digits

class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits
    @staticmethod
    def check_card_number(number):
        if '-' not in number:
            return False
        lst = number.split('-')
        if len(lst) != 4:
            return False
        for row in lst:
            if len(row) != 4:
                return False
            for char in row:
                if char not in digits:
                    return False
        return True
    
    
    @staticmethod
    def check_name(name):
        if ' ' not in name:
            return False
        a = name.split()
        if len(a) != 2:
            return False
        for row in a:
            for char in row:
                if char not in CardCheck.CHARS_FOR_NAME:
                    return False
        return True