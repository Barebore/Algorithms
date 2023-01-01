import unittest


class Calculator:
    """Производит арифметические действия."""

    def summ(self, *args):
        """Возвращает сумму принятых аргументов."""       
        print(len(args))
        print(args)
        return (sum(i for i in args)) if len(args) > 1 else None


class TestCalc(unittest.TestCase):
    """Тестируем Calculator."""
    
    @classmethod
    def setUpClass(cls):
        """Вызывается однажды перед запуском всех тестов класса."""
        cls.calc = Calculator()

    def test_summ(self):
        act = TestCalc.calc.summ(3, -3, 5)
        self.assertEqual(act, 5, 'summ работает неправильно')

    def test_summ_no_argument(self):
        self.assertIsNone(self.calc.summ())

    def test_summ_one_argument(self):
        a = 1
        self.assertIsNone(self.calc.summ(a))

# if __name__ == '__main__':
#     unittest.main()


calc = Calculator

print(calc.summ(6,3,3))