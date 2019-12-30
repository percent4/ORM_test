# -*- coding: utf-8 -*-
# author: Jclian91
# place: Sanya, Hainan
# time: 12:52

from create_table import Users
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def query_data():
    # 初始化数据库连接
    engine = create_engine("mysql+pymysql://root:@localhost:3306/orm_test", encoding="utf-8")
    # 创建DBSession类型
    DBSession = sessionmaker(bind=engine)

    # 创建session对象
    session = DBSession()

    # 查询所有place是CHN的人名
    # 创建Query查询，filter是where条件
    # 调用one()返回唯一行，如果调用all()则返回所有行:
    users = session.query(Users).filter(Users.place == 'CHN').all()
    print([use.name for use in users])
    # 输出：['Chen', 'Zhang']

    # 或者用如下查询
    users = session.query(Users.name).filter(Users.place == 'CHN').all()
    print(users)
    # 输出：[('Chen',), ('Zhang',)]

    session.close()


if __name__ == '__main__':
    query_data()