# Проблема в том, что в lambda функцию не передается step

from typing import Callable

def create_handlers(callback):
   handlers = []
   for step in range(5):
      # добавляем обработчики для каждого шага (от 0 до 4)
      handlers.append(callback(step))
   return handlers

def execute_handlers(handlers):
  # запускаем добавленные обработчики (шаги от 0 до 4)
  for handler in handlers:
    handler()

def func1(a):
   print(a)

handlers = create_handlers(func1)
execute_handlers(handlers)


