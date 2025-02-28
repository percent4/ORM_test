# -*- coding: utf-8 -*-
# @place: Pudong, Shanghai
# @file: sqlmodel_async_crud.py
# @time: 2025/2/28 20:12
# 使用SQLModel异步CRUD操作
import asyncio
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from sqlalchemy.ext.asyncio import create_async_engine

from src.models.sqlmodel_create_table import Users

# 初始化数据库连接
async_engine = create_async_engine("mysql+aiomysql://root:root@localhost:3306/orm_test")
async_session = AsyncSession(async_engine)


async def insert_data():
    async with async_session as db_session:
        async with db_session.begin():
            # 插入单条数据
            entity = {'name': 'Jack', 'age': 25, 'place': 'USA'}
            db_session.add(Users(**entity))
            print("插入1条数据")

    async with async_session as db_session:
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
    async with async_session as db_session:
        async with db_session.begin():
            # 查询第1条数据
            print("查询第1条数据")
            statement = select(Users)
            user = await db_session.exec(statement)
            print(user.first())
            # 查询所有数据
            print("查询所有数据")
            statement = select(Users)
            users = await db_session.exec(statement)
            for u in users.all():
                print(u)
            # 查询指定字段
            print("查询指定字段: name and age")
            statement = select(Users.name, Users.age)
            users = await db_session.exec(statement)
            print(users.all())
            # 条件查询1
            print("条件查询: age > 30")
            statement = select(Users).where(Users.age > 30)
            users = await db_session.exec(statement)
            for u in users.all():
                print(u)
            # 条件查询2
            print("条件查询: age > 50 and place == 'CHN'")
            statement = select(Users).where(Users.age > 50).where(Users.place == 'CHN')
            users = await db_session.exec(statement)
            for u in users.all():
                print(u)
            # 排序查询
            print("排序查询")
            statement = select(Users).order_by(Users.age)
            users = await db_session.exec(statement)
            for u in users.all():
                print(u)


async def update_data():
    async with async_session as db_session:
        async with db_session.begin():
            # 更新数据
            # 1. 查询数据
            statement = select(Users).where(Users.name == 'Zhang')
            result = await db_session.exec(statement)
            user = result.first()
            print("更新前数据: ", user)
            # 2. 更新数据
            user.age = 45
            db_session.add(user)
        await db_session.commit()

        async with db_session.begin():
            # 3. 再次查询数据
            statement = select(Users).where(Users.name == 'Zhang')
            user = await db_session.exec(statement)
            print("更新后数据: ", user.first())


async def delete_data():
    async with async_session as db_session:
        async with db_session.begin():
            # 删除数据
            # 1. 查询数据
            statement = select(Users).where(Users.name == 'Zhang')
            result = await db_session.exec(statement)
            user = result.first()
            print("删除前数据: ", user)
            # 2. 删除数据
            await db_session.delete(user)
        await db_session.commit()
        # 3. 再次查询数据
        async with db_session.begin():
            statement = select(Users).where(Users.name == 'Zhang')
            user = await db_session.exec(statement)
            print("删除后数据: ", user.first())


if __name__ == '__main__':
    # 异步插入数据
    # print("异步插入数据")
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(insert_data())
    # 异步查询数据
    # print("异步查询数据")
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(query_data())
    # 异步更新数据
    # print("异步更新数据")
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(update_data())
    # 异步删除数据
    print("异步删除数据")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(delete_data())


