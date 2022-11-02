import sqlite3

con = sqlite3.connect('db.sqlite')

cur = con.cursor()

cur.execute('''
-- Верни все поля
SELECT *
-- из таблицы movies
FROM movies
-- ...но перед этим присоедини таблицу slogans так, чтобы в записях
-- совпадали значения полей movies.slogan_id и slogans.id
JOIN slogans ON movies.slogan_id = slogans.id; 
''')
i = 0
for value in cur:
    i += 1
    print(i, value)
con.commit()
con.close()

