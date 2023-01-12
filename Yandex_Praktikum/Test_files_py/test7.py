from typing import Any


def ultimate_answer(question: Any) -> int:
    """Выводит на печать переданный аргумент и возвращает 42."""
    print(f'Ваш вопрос: {question}')
    return 42

assert ultimate_answer('Что делать?') == 42, (
    'Вызов ultimate_answer("Что делать?") '
    'не вернул ожидаемый результат'
)

result = ultimate_answer('Кому на Руси жить хорошо?')
assert(result == 42,
       'Вызов ultimate_answer("Кому на Руси жить хорошо?") '
       'не вернул ожидаемый результат'
)