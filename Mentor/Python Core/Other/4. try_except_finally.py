try:
    print('lets')
    # пытаемся сделать
except:
    raise ValueError('BEDA')
    # если сделать не вышло, выбрасываем исключение
finally:
    print('finally')
    # делаем всегда по окончанию 