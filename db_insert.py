# -*- coding: utf-8 -*-
# author: Jclian91
# place: Sanya, Hainan
# time: 12:52

from create_table import Users
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def insert_data():
    # 初始化数据库连接
    engine = create_engine("mysql+pymysql://root:@localhost:3306/orm_test", encoding="utf-8")
    # 创建DBSession类型
    DBSession = sessionmaker(bind=engine)

    # 创建session对象
    session = DBSession()
    # 插入单条数据
    # 创建新User对象
    new_user = Users(id=1, name='Jack', age=25, place='USA')
    # 添加到session
    session.add(new_user)
    # 提交即保存到数据库
    session.commit()

    # 插入多条数据
    user_list= [Users(id=2, name='Green', age=26, place='UK'),
                Users(id=3, name='Alex', age=31, place='GER'),
                Users(id=4, name='Chen', age=52, place='CHN'),
                Users(id=5, name='Zhang', age=42, place='CHN')
               ]
    session.add_all(user_list)
    session.commit()
    # 关闭session
    session.close()
    print('insert into db successfully!')

if __name__ == '__main__':
    insert_data()