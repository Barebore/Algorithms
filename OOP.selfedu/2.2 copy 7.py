class PhoneBook:
    
    def __init__(self):
        self.phone_list = []

    def add_phone(self, obj):
        self.phone_list.append(obj)

    def remove_phone(self, index):
        del self.phone_list[index]

    def get_phone_list(self):
        return self.phone_list

class PhoneNumber:
    def __init__(self, number, fio):
        self.number = number
        self.fio = fio

p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
phones = p.get_phone_list()
print(phones)