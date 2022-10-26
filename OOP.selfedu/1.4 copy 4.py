class Translator:
    dict = {}
    
    def add(self, eng, rus):
        if eng in self.dict:
            if rus in self.dict[eng]:
                return
            else:
                self.dict[eng].append(rus)
        else:
            self.dict[eng] = []
            self.dict[eng].append(rus)
    
    def remove(self, eng):
        del self.dict[eng]
    
    def translate(self, eng):
        return self.dict[eng]

tr = Translator()

tr.add("tree", "дерево")
tr.add("car", "машина")
tr.add("car", "автомобиль")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("milk", "молоко")

print(tr.dict)

tr.remove('car')

print(tr.dict)

print(*tr.translate('go'))