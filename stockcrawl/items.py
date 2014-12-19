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
    deal_count = scrapy.Field()  # 总成交量（手）
    deal_amount = scrapy.Field()  # 总成交额（万）
    up_num = scrapy.Field()  # 领涨股数量
    up_per = scrapy.Field()  # 涨跌幅
    up_current_price = scrapy.Field()  # 当前价
    up_price = scrapy.Field()  # 涨跌额
    up_code = scrapy.Field()  # 领涨股


class StockItem(scrapy.Item):
    code = scrapy.Field()  # 股票代码
    name = scrapy.Field()  # 股票名字
    i_code = scrapy.Field()  # 行业code
    trade = scrapy.Field()  #
    pricechange = scrapy.Field()  #
    changepercent = scrapy.Field()  #
    ticktime = scrapy.Field()  #
    pb = scrapy.Field()  #
    turnoverratio = scrapy.Field()  #
