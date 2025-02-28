# -*- coding: utf-8 -*-
# @place: Pudong, Shanghai
# @file: sqlalchemy_init_db.py
# @time: 2025/2/28 11:29
from src.models.sqlalchemy_db import Base, engine
from src.models.sqlalchemy_school import School
from src.models.sqlalchemy_student import Student

# 创建表
Base.metadata.create_all(bind=engine)
print('Create table successfully!')
