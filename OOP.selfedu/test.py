# def remove_duplicates(lst):
#     # Преобразование словарей в кортежи
#     tuples_lst = [tuple(d.items()) for d in lst]
#     print(tuples_lst)

#     # Создание множества для удаления дубликатов
#     tuples_set = set(tuples_lst)
#     print(tuples_lst)

#     # Преобразование кортежей обратно в словари
#     result = [dict(t) for t in tuples_set]

#     return result

# print(remove_duplicates([{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, {}, {}, {"key1": "value1"}, {"key1": "value1"}, {"key2": "value2"}]))

a = [0] * 10
print(a)