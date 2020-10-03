from database import Database
from os import getenv
import click




@click.group()
def cli():
    pass




@click.command()
def setup():
    print('I create new DataBase')
    db = Database(getenv('DB_NAME'))
    db.create_table('''CREATE TABLE URL_Storage
                         (id INTEGER PRIMARY KEY AUTOINCREMENT,
                          category text,
                           url text)''')

@click.command()
@click.argument('category')
@click.argument('url')
def add(category, url):
    print('I added new URL')
    db = Database(getenv('DB_NAME'))
    db.insert('URL_Storage', None, category, url)

@click.command()
def category_list():
    print('This is list of categories')
    db = Database(getenv('DB_NAME'))
    categories = db.fetch_distinct('URL_Storage','category')
    for name in categories:
        print(name)

@click.command()
@click.argument('category_name')
def category(category_name):
    print('List of url\'s from category: [' + str(category_name) + ']')
    db = Database(getenv('DB_NAME'))
    urls = db.display('URL_Storage', category=category_name)
    for url in urls:
        print(url[2])



