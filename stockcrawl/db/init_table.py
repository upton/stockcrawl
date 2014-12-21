#!/usr/bin/env python
# -*- coding: utf-8 -*-

from stockcrawl.db import Base, engine, models

Base.metadata.create_all(engine)
