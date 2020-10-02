import sqlite3

connect = sqlite3.connect(r'D:\STUDIA\Programowanie\DATA_BASE\Analityka_Edu_SQLite\birthdays.sqlite')

cur = connect.cursor()

for items in cur.execute('SELECT * FROM birthday ORDER BY name'):
    print(items)

connect.close
