list = [i for i in range(20)]
print(list)


dct = {i: i * i for i in range(5)}
print(dct)


fruits = {'apple': 5, 'banana': 6, 'cherry': 6, 'date': 4, 'elderberry': 10}
b_fruits = {k: v for k, v in fruits.items() if k.startswith('b')}
print(b_fruits)