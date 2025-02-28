# -*- coding: utf-8 -*-
# @place: Pudong, Shanghai
# @file: sqlalchemy_school.py
# @time: 2025/2/28 11:31
from datetime import datetime as dt
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, DATETIME

from src.models.sqlalchemy_db import Base


class School(Base):

    __tablename__ = 'school'

    id = Column(INTEGER, primary_key=True, autoincrement=True)
    insert_time = Column(DATETIME, default=dt.now())
    update_time = Column(DATETIME, default=dt.now(), onupdate=dt.now())
    is_deleted = Column(INTEGER, default=0)
    name = Column(VARCHAR(256), nullable=False)
    address = Column(VARCHAR(256), nullable=False)
    phone = Column(VARCHAR(256), nullable=False)
