class Model:
    def query(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        result = 'Model'
        if self.__dict__:
            result += ': ' + ', '.join(f"{k} = {v}" for k, v in self.__dict__.items())
        return result
    
model = Model()
# model.query(id=1, fio='Sergey', old=33)
print(model)