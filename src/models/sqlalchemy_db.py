# -*- coding: utf-8 -*-
# @place: Pudong, Shanghai
# @file: sqlalchemy_db.py
# @time: 2025/2/28 12:59
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

# 创建MySQL数据库引擎
DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/orm_test"
engine = create_engine(DATABASE_URL, echo=True)

# 创建共享的 Base 类
Base = declarative_base()
