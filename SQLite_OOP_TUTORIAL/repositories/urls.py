from database import Database
from os import getenv

def save(category: str, url: str):
    db = Database(getenv('DB_NAME'))
    db.insert('URL_Storage', None, category, url)


def list_categories():
    db = Database(getenv('DB_NAME'))
    return db.fetch_distinct('URL_Storage','category')


def list_urls(category_name):
    db = Database(getenv('DB_NAME'))
    return db.display('URL_Storage', category=category_name)




