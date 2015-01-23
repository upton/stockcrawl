# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

'''
行业Item
'''
class IndustryItem(scrapy.Item):
    code = scrapy.Field()  # 行业Code
    name = scrapy.Field()  # 行业名称
    companys = scrapy.Field()  # 公司家数
    price_avg = scrapy.Field()  # 平均价格
    updn_price = scrapy.Field()  # 涨跌额
    updn_per = scrapy.Field()  # 涨跌幅
    up_code = scrapy.Field()  # 领涨股


class StockItem(scrapy.Item):
    code = scrapy.Field()  # 股票代码
    name = scrapy.Field()  # 股票名字
    icode = scrapy.Field()  # 行业code
    price = scrapy.Field()  # 价格
    totalShares = scrapy.Field()  # 总股本：122.60亿
    float_shares = scrapy.Field()  # 流通股本：101.26亿
    eps = scrapy.Field()  # 每股收益：0.35
    dividend = scrapy.Field()  # 每股股息：0.20
    net_assets = scrapy.Field()  # 每股净资产：3.87
    pe_lyr = scrapy.Field()  # 市盈率LYR：40.88
    pe_ttm = scrapy.Field()  # 市盈率TTM：30.32
    pb = scrapy.Field()  # 市净率TTM：3.64
    psr = scrapy.Field()  # 市销率TTM：1.62
    
    
