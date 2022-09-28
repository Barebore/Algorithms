city = tuple(input().split())
new_city = ()
if 'Ульяновск' in city:
    for i in range(len(city)):
        if i == city.index('Ульяновск'):
            continue
        else:
            new_city += (city[i],)
else:
    new_city = city
print(*new_city)
