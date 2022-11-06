class Car:

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if type(model) == str and 100 >= len(model) >= 2:
            self.__model = model
    

car = Car()
car.model = 'Toyota'
    