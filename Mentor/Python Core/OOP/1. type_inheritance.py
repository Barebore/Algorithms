#виды наследования в Python

'''
Одиночное наследование (single inheritance): это наследование, когда класс наследует от одного базового класса.
Для выполнения одиночного наследования необходимо указать имя базового класса в определении наследуемого класса.
'''

class BaseClass:
    pass

class DerivedClass(BaseClass):
    pass


'''
Множественное наследование (multiple inheritance): это наследование, когда класс наследует от
нескольких базовых классов. Для выполнения множественного наследования необходимо указать имена
базовых классов через запятую в определении наследуемого класса.
'''


class BaseClass1:
    pass

class BaseClass2:
    pass

class DerivedClass(BaseClass1, BaseClass2):
    pass


'''
Абстрактное наследование (abstract inheritance): это наследование, когда класс наследует только интерфейс
базового класса, но не его реализацию. Для выполнения абстрактного наследования в Python используются абстрактные
классы, которые могут содержать абстрактные методы (методы без реализации).
'''

from abc import ABC, abstractmethod

class BaseClass(ABC):
    @abstractmethod
    def some_method(self):
        pass

class DerivedClass(BaseClass):
    def some_method(self):
        # реализация метода
        pass

