import click
from database import Database
from os import getenv,getcwd
from repositories.urls import save, list_categories, list_urls





@click.group()
def cli():
    pass




@click.command(name='setup')
def setup():
    print('I create new DataBase')
    db = Database(getenv('DB_NAME'))
    db.create_table('''CREATE TABLE URL_Storage
                         (id INTEGER PRIMARY KEY AUTOINCREMENT,
                          category text,
                           url text)''')

@click.command(name='add')
@click.argument('category')
@click.argument('url')
def add(category: str, url: str):
    print('I added new URL')
    save(category, url)

@click.command(name = 'categories')
def category_list():
    print('This is list of categories')
    for name in list_categories():
        print(name[0])

@click.command(name='category')
@click.argument('category_name')
def category(category_name: str):
    print('List of url\'s from category: [' + category_name + ']')
    for url in list_urls(category_name):
        print(url[2])



