# put your python code here
t = ["– Скажи-ка, дядя, ведь не даром",
    "Я Python выучил с каналом",
    "Балакирев что раздавал?",
    "Ведь были ж заданья боевые,",
    "Да, говорят, еще какие!",
    "Недаром помнит вся Россия",
    "Как мы рубили их тогда!"
    ]
a = [row.split() for row in t]
for i,x in enumerate(a):
    index = []
    for j, y in enumerate(x):
        if len(y) <= 3:
            index.append(j)
   # print(index)
    k = 0
    for count in index:
        a[i].pop(count-k)
        k += 1
        
    index = []
print(a)

# put your python code here
t = ["– Скажи-ка, дядя, ведь не даром",
    "Я Python выучил с каналом",
    "Балакирев что раздавал?",
    "Ведь были ж заданья боевые,",
    "Да, говорят, еще какие!",
    "Недаром помнит вся Россия",
    "Как мы рубили их тогда!"
    ]

a = [[x for x in row.split() if len(x) > 3]for row in t] 
print(a)






