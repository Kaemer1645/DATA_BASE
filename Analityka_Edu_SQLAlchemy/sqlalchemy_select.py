import sqlalchemy_base

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind = sqlalchemy_base.engine)
session = Session()

#all data

for s in session.query(sqlalchemy_base.Transaction).all():
    print(s.transaction_id)


#chosen data

for s in session.query(sqlalchemy_base.Transaction).filter(sqlalchemy_base.Transaction.transaction_id>5):
    print(s.transaction_id)