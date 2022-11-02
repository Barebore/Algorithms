import sqlite3

con = sqlite3.connect('db.sqlite')

cur = con.cursor()

cur.executescript('''
SELECT *
FROM sqlite_master 
''')
for i in cur:
    print(i)
con.commit()
con.close()