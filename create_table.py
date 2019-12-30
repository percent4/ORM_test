# -*- coding: utf-8 -*-
# author: Jclian91
# place: Sanya, Hainan
# time: 12:46

from sqlalchemy.dialects.mysql import INTEGER, VARCHAR
from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'

    id = Column(INTEGER, primary_key=True)
    name = Column(VARCHAR(256), nullable=False)
    age = Column(INTEGER)
    place = Column(VARCHAR(256), nullable=False)


    def __init__(self, id, name, age, place):
        self.id = id
        self.name = name
        self.age = age
        self.place = place

def init_db():
    engine = create_engine(
        "mysql+pymysql://root:@localhost:3306/orm_test",
        encoding= "utf-8",
        echo=True
    )
    Base.metadata.create_all(engine)
    print('Create table successfully!')

if __name__ == '__main__':
    init_db()