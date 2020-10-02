from database import Database

from sys import argv
from os import getenv
from dotenv import load_dotenv
load_dotenv()






if len(argv) == 2 and  argv[1] == 'setup':
    '''
        Initialize DataBase
        Usage: python main.py setup
    '''
    print('I create new DataBase')
    db = Database(getenv('DB_NAME'))
    db.create_table('''CREATE TABLE URL_Storage
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      category text,
                       url text)''')

if len(argv) == 4 and argv[1] == 'add':
    '''
    Adding new variable
    Usage: python main.py add --category-- http://google.com
    '''
    print('I added new URL')
    category = argv[2]
    url = argv[3]
    db = Database(getenv('DB_NAME'))
    db.insert('URL_Storage',None,category,url)

if len(argv) == 3 and argv[1] == 'category':
    '''
    Search data by category
    Usage: python main.py catergory --category name--
    '''
    category_name = argv[2]
    print('List of url\'s from category: ['+str(category_name)+']')
    db = Database(getenv('DB_NAME'))
    urls = db.display('URL_Storage', category = category_name)
    for url in urls:
        print(url[2])



