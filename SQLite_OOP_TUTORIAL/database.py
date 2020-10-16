import sqlite3


class Database:
    def __init__(self,database_name):
        # create class properties by add self to local variable
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()


        #object doesn't exist when: - we delete variable, script finished and when we add something to our variable which storage something different

    def __del__(self):
        self.connection.close()

    def create_table(self, sql: str):
        self.cursor.execute(sql)
        self.connection.commit()

    def insert(self,table,*args):
        self.cursor.execute(f"INSERT INTO {table} VALUES ({','.join(['?' for _ in args])})",args)
        self.connection.commit()

    def display(self,table, **kwargs):
        query = self.cursor.execute(f"SELECT * FROM {table} WHERE {' and '.join([f'{kwarg}=?' for kwarg in kwargs])}", tuple(kwargs.values()))
        return query.fetchall()

    def fetch_distinct(self, table, column):
        query = self.cursor.execute(f"SELECT DISTINCT {column} FROM {table}")
        return query.fetchall()

