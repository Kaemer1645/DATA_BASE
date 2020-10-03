#SQLAlchemy tutorial

#import objects from sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#initilize connect with DataBase

engine = create_engine(r'sqlite:///D:\STUDIA\Programowanie\DATA_BASE\Analityka_Edu_SQLAlchemy\sqlalchemy.sqlite', echo = True)

#managment tables

base = declarative_base()



#define class which is storage users in DataBase


class Transaction(base):

    __tablename__ = 'Transactions'

    transaction_id = Column(Integer, primary_key=True)
    data = Column(String)
    item_id = Column(Integer)
    price = Column(Integer)

    def __init__(self, transaction_id, data, item_id, price):
        self.transaction_id = transaction_id
        self.data = data
        self.item_id = item_id
        self.price = price


base.metadata.create_all(engine)