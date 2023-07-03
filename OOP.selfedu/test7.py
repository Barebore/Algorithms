# Все функции в списке handlers будут ссылаться на значение step=4.
# Добавив параметр по умолчанию избежим данной проблемы, путём создания каждый раз нового экземпляра, т.е. создавая новую область видимости.
from typing import Callable, List

def create_handlers(callback: Callable[[int], None]) -> List[Callable[[], None]]:
   handlers = []
   for step in range(5):
      handlers.append(lambda step=step: callback(step))
   return handlers

def execute_handlers(handlers: List[Callable[[], None]]) -> None:
  for handler in handlers:
     handler()

