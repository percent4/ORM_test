# -*- coding: utf-8 -*-
# @place: Pudong, Shanghai
# @file: sqlalchemy_crud.py
# @time: 2025/2/28 10:57
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

from src.models.sqlalchemy_create_table import Users

# 初始化数据库连接
engine = create_engine("mysql+pymysql://root:root@localhost:3306/orm_test")
DBSession = sessionmaker(bind=engine)
session = DBSession()


# 封装为上下文管理器
@contextmanager
def session_maker(session=session):
    try:
        yield session
        session.commit()
    except Exception: # noqa
        session.rollback()
        raise
    finally:
        session.close()


def insert_data():
    with session_maker() as db_session:
        # 插入单条数据
        entity = {'name': 'Jack', 'age': 25, 'place': 'USA'}
        db_session.add(Users(**entity))
        print("插入1条数据")

    with session_maker() as db_session:
        # 插入多条数据
        users = [
            {"name": "Green", "age": 26, "place": "UK"},
            {"name": "Alex", "age": 31, "place": "GER"},
            {"name": "Chen", "age": 52, "place": "CHN"},
            {"name": "Zhang", "age": 42, "place": "CHN"}
        ]
        entities = [Users(**user) for user in users]
        db_session.add_all(entities)
        print(f"插入{len(entities)}条数据")


def query_data():
    with session_maker() as db_session:
        # 查询第1条数据
        print("查询第1条数据")
        user = db_session.query(Users).first()
        print(user)
        # 查询所有数据
        print("查询所有数据")
        users = db_session.query(Users).all()
        for u in users:
            print(u)
        # 查询指定字段
        print("查询指定字段: name, age")
        user = db_session.query(Users.name, Users.age).all()
        print(user)
        # 条件查询1
        print("条件查询: age > 30")
        user = db_session.query(Users).filter(Users.age > 30).all()
        print(user)
        # 条件查询2
        print("条件查询: age > 50 and place == 'CHN'")
        user = db_session.query(Users).filter(Users.age > 50, Users.place == 'CHN').all()
        print(user)
        # 排序查询
        print("排序查询")
        user = db_session.query(Users).order_by(Users.age.desc()).all()
        print(user)


def update_data():
    with session_maker() as db_session:
        # 更新数据
        # 1. 查询数据
        user = db_session.query(Users).filter(Users.name == 'Zhang').first()
        print("更新前数据: ", user)
        # 2. 更新数据
        user.age = 45
        db_session.flush()
        # 3. 再次查询数据
        user = db_session.query(Users).filter(Users.name == 'Zhang').first()
        print("更新后数据: ", user)


def delete_data():
    with session_maker() as db_session:
        # 删除数据
        # 1. 查询数据
        user = db_session.query(Users).filter(Users.name == 'Zhang').first()
        print("删除前数据: ", user)
        # 2. 删除数据
        db_session.delete(user)
        db_session.flush()
        # 3. 再次查询数据
        user = db_session.query(Users).filter(Users.name == 'Zhang').first()
        print("删除后数据: ", user)


if __name__ == '__main__':
    print('*' * 20, '插入数据', '*' * 20)
    insert_data()
    print('*' * 20, '查询数据', '*' * 20)
    query_data()
    print('*' * 20, '更新数据', '*' * 20)
    update_data()
    print('*' * 20, '删除数据', '*' * 20)
    delete_data()
