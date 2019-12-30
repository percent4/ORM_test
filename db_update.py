# -*- coding: utf-8 -*-
# author: Jclian91
# place: Sanya, Hainan
# time: 12:52

from create_table import Users
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def update_data():
    # 初始化数据库连接
    engine = create_engine("mysql+pymysql://root:@localhost:3306/orm_test", encoding="utf-8")
    # 创建DBSession类型
    DBSession = sessionmaker(bind=engine)

    # 创建session对象
    session = DBSession()

    # 数据更新，将Jack的place修改为CHN
    update_obj = session.query(Users).filter(Users.name=='Jack').update({"place":"CHN"})
    session.commit()

    session.close()
    print("Update data successfully!")


if __name__ == '__main__':
    update_data()