def simple_bulk_create(model, objects):
    # Получим информацию о модели
    table = model._meta.db_table
    fields = model._meta.fields

    # Сформируем SQL запрос
    field_names = ', '.join(field.name for field in fields)
    placeholders = ', '.join('%s' for _ in fields)
    sql = f'INSERT INTO {table} ({field_names}) VALUES ({placeholders})'

    # Соберем данные для каждого объекта
    data = [
        [getattr(obj, field.name) for field in fields]
        for obj in objects
    ]

    # Выполним запрос для каждого объекта
    with connection.cursor() as cursor:
        for params in data:
            cursor.execute(sql, params)