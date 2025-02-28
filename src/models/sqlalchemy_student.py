# -*- coding: utf-8 -*-
# @place: Pudong, Shanghai
# @file: sqlalchemy_student.py
# @time: 2025/2/28 11:32
from datetime import datetime as dt
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, DATETIME

from src.models.sqlalchemy_db import Base


class Student(Base):
    __tablename__ = 'student'

    id = Column(INTEGER, primary_key=True, autoincrement=True)
    insert_time = Column(DATETIME, default=dt.now())
    update_time = Column(DATETIME, default=dt.now(), onupdate=dt.now())
    is_deleted = Column(INTEGER, default=0)
    name = Column(VARCHAR(256), nullable=False)
    age = Column(VARCHAR(256), nullable=False)
    gender = Column(VARCHAR(10), nullable=False)
