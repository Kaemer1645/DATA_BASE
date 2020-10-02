import sqlite3

#connect to base
connect = sqlite3.connect(r'D:\STUDIA\Programowanie\DATA_BASE\Analityka_Edu_SQLite\birthdays.sqlite')

#create cursor
cur = connect.cursor()

#create dict
dict = {'Justyna':'08-04-1998','Szymon':'11-02-1997','Amadeusz':'11-11-2001'}
#create table

cur.execute('''CREATE TABLE birthday
             (name TEXT, birthday TEXT)''')

'''cur.execute("""INSERT INTO transakcje VALUES 
        ('2020-05-06', 36, 17.50)""")'''

#cur.execute("""INSERT INTO birthday VALUES
        #('2020-05-06','kot')""")


with connect:
    for name,date in dict.items():
        cur.execute("""INSERT INTO birthday VALUES(?, ?)""", (name, date))

#post data



#save changes
connect.commit()
#close connection with db
connect.close()