#!/usr/bin/env python
# -*- coding: utf-8 -*-

from stockcrawl.db import Base
from sqlalchemy import Column, Integer, String, Numeric, DateTime

class Industry(Base):
    __tablename__ = 'industry'
    code = Column(String(16), primary_key=True)  # 行业Code
    name = Column(String(32))  # 行业名称
    companys = Column(Integer)  # 公司家数
    price_avg = Column(Numeric(10, 3))  # 平均价格
    updn_price = Column(Numeric(6, 3))  # 涨跌额
    updn_per = Column(Numeric(6, 3))  # 涨跌幅
    up_code = Column(String(16))  # 领涨股
    create_time = Column(DateTime)  # 创建时间
    update_time = Column(DateTime)  # 更新时间

    def __repr__(self):
        return '<Industry %s:%s>' % (self.code, self.name)

class Stock(Base):
    __tablename__ = 'stock'
    code = Column(String(16), primary_key=True)  # 股票代码
    name = Column(String(16))  # 股票名字
    icode = Column(String(16))  # 行业code
    price = Column(Numeric(10, 3))  # 价格
    create_time = Column(DateTime)  # 创建时间
    update_time = Column(DateTime)  # 更新时间

    def __repr__(self):
        return '<Stock %s:%s>' % (self.code, self.name)
