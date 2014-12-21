# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from items import IndustryItem, StockItem
from stockcrawl.db import Session
from stockcrawl.db.models import Industry, Stock
from datetime import datetime

class StockcrawlPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, IndustryItem):
            ######IndustryItem
            self.save_industry(item)
        elif isinstance(item, StockItem):
            ######StockItem
            self.save_stock(item)
            
        return item
    
    def save_industry(self, item):
        industry = Industry(code=item['code'],
                            name=item['name'],
                            companys=item['companys'],
                            price_avg=item['price_avg'],
                            updn_price=item['updn_price'],
                            updn_per=item['updn_per'],
                            up_code=item['up_code'],
                            update_time=datetime.now())
        
        ses = Session()
        industry = ses.merge(industry)
        
        if not industry.create_time:
            industry.create_time = datetime.now()
        
        ses.commit()
        
        
    def save_stock(self, item):
        stock = Stock()
        if item.get('icode'):
            stock = Stock(code=item['code'],
                          icode=item['icode'],
                          update_time=datetime.now())
        else:
            stock = Stock(code=item['code'],
                          name=item['name'],
                          price=item['price'],
                          update_time=datetime.now())
        
        ses = Session()
        stock = ses.merge(stock)
        
        if not stock.create_time:
            stock.create_time = datetime.now()
            
        ses.commit()
