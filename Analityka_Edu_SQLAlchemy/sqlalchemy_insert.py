import sqlalchemy_base

from sqlalchemy.orm import sessionmaker

#create new session

Session = sessionmaker(bind=sqlalchemy_base.engine)
session = Session()

#add data

for i in range(10):
    tr = sqlalchemy_base.Transaction(i, '2020/10/03',i+1,19.50)
    session.add(tr)


session.commit()


