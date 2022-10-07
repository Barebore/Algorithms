from string import ascii_lowercase


gen = (i+j for i in ascii_lowercase for j in ascii_lowercase)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

# put your python code here
cities = ["Москва", "Ульяновск", "Самара", "Уфа", "Омск", "Тула"]

gen = (i for i in cities*1000000)
for i in range(20):
    print(next(gen), end = ' ' )