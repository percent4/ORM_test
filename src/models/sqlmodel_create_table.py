# -*- coding: utf-8 -*-
# @place: Pudong, Shanghai
# @file: sqlmodel_create_table.py
# @time: 2025/2/28 10:55
from datetime import datetime as dt
from sqlmodel import Field, SQLModel, create_engine


class Users(SQLModel, table=True):
    # add table name
    __tablename__ = "users"
    id: int = Field(primary_key=True, nullable=False)
    name: str = Field(nullable=False)
    age: int = Field(nullable=True)
    place: str = Field(nullable=True)
    insert_time: dt = Field(nullable=True, default=dt.now())

    def __repr__(self):
        return f"Users(id={self.id}, name={self.name}, age={self.age}, place={self.place})"


if __name__ == '__main__':
    # 创建数据库引擎
    sqlite_url = "mysql+pymysql://root:root@localhost:3306/orm_test"
    engine = create_engine(sqlite_url, echo=True)

    # 创建所有表
    SQLModel.metadata.create_all(engine)
    # 删除所有表
    # SQLModel.metadata.drop_all(engine)
