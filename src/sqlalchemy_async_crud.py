# -*- coding: utf-8 -*-
# @place: Pudong, Shanghai
# @file: sqlalchemy_async_crud.py
# @time: 2025/2/28 19:45
# 使用SQLAlchemy异步操作数据库
import asyncio
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from src.models.sqlalchemy_create_table import Users

# 初始化数据库连接
async_engine = create_async_engine("mysql+aiomysql://root:root@localhost:3306/orm_test")
async_session = sessionmaker(bind=async_engine, class_=AsyncSession)


async def insert_data():
    async with async_session() as db_session:
        async with db_session.begin():
            # 插入单条数据
            entity = {'name': 'Jack', 'age': 25, 'place': 'USA'}
            db_session.add(Users(**entity))
            print("插入1条数据")

        async with db_session.begin():
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


async def query_data():
    async with async_session() as db_session:
        async with db_session.begin():
            # 查询第1条数据
            print("查询第1条数据")
            statement = select(Users)
            user = await db_session.execute(statement)
            print(user.first())
            # 查询所有数据
            print("查询所有数据")
            statement = select(Users)
            users = await db_session.execute(statement)
            for u in users.scalars():
                print(u)
            # 查询指定字段
            print("查询指定字段: name and age")
            statement = select(Users.name, Users.age)
            users = await db_session.execute(statement)
            print(users.all())
            # 条件查询1
            print("条件查询: age > 30")
            statement = select(Users).where(Users.age > 30)
            users = await db_session.execute(statement)
            for u in users.scalars():
                print(u)
            # 条件查询2
            print("条件查询: age > 50 and place == 'CHN'")
            statement = select(Users).where((Users.age > 50) & (Users.place == 'CHN'))
            users = await db_session.execute(statement)
            for u in users.scalars():
                print(u)
            # 排序查询
            print("排序查询")
            statement = select(Users).order_by(Users.age.desc())
            users = await db_session.execute(statement)
            for u in users.scalars():
                print(u)


async def update_data():
    async with async_session() as db_session:
        async with db_session.begin():
            # 更新数据
            # 1. 查询数据
            statement = select(Users).where(Users.name == 'Zhang')
            user = await db_session.execute(statement)
            user = user.scalars().first()
            print("更新前数据: ", user)
            # 2. 更新数据
            user.age = 45
            # 3. 再次查询数据
            statement = select(Users).where(Users.name == 'Zhang')
            user = await db_session.execute(statement)
            user = user.scalars().first()
            print("更新后数据: ", user)


async def delete_data():
    async with async_session() as db_session:
        async with db_session.begin():
            # 删除数据
            # 1. 查询数据
            statement = select(Users).where(Users.name == 'Zhang')
            user = await db_session.execute(statement)
            user = user.scalars().first()
            print("删除前数据: ", user)
            # 2. 删除数据
            await db_session.delete(user)
            # 3. 再次查询数据
            statement = select(Users).where(Users.name == 'Zhang')
            user = await db_session.execute(statement)
            user = user.scalars().first()
            print("删除后数据: ", user)


if __name__ == '__main__':
    # 异步插入数据
    print("异步插入数据")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(insert_data())
    # 异步查询数据
    print("异步查询数据")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(query_data())
    # 异步更新数据
    print("异步更新数据")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(update_data())
    # 异步删除数据
    print("异步删除数据")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(delete_data())
