from typing import Any


def ultimate_answer(question: Any) -> str:
    """Выводит на печать переданный аргумент и возвращает строку ответа.
    >>> ultimate_answer('Two beer, or not two beer?')
    42
    """
    print(f'Ваш вопрос: {question}')
    return f'Ответ на ваш вопрос "{question}": 42'


# При запуске файла выполнить доктест
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    ultimate_answer('Продолжим работать?')