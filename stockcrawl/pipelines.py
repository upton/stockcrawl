# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from items import IndustryItem, StockItem

class StockcrawlPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, IndustryItem):
            print '######IndustryItem:', item
        elif isinstance(item, StockItem):
            print '######StockItem:', item
            
        return item