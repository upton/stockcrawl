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
    totalShares = Column(String(16))  # 总股本：122.60亿
    float_shares = Column(String(16))  # 流通股本：101.26亿
    eps = Column(String(16))  # 每股收益：0.35
    dividend = Column(String(16))  # 每股股息：0.20
    net_assets = Column(String(16))  # 每股净资产：3.87
    pe_lyr = Column(Numeric(12, 4))  # 市盈率LYR：40.88
    pe_ttm = Column(Numeric(12, 4))  # 市盈率TTM：30.32
    pb = Column(Numeric(12, 4))  # 市净率TTM：3.64
    psr = Column(Numeric(12, 4))  # 市销率TTM：1.62
    create_time = Column(DateTime)  # 创建时间
    update_time = Column(DateTime)  # 更新时间

    def __repr__(self):
        return '<Stock %s:%s>' % (self.code, self.name)
