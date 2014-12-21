#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql://stock:zaq12wsx@localhost/stock?charset=utf8', convert_unicode=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
