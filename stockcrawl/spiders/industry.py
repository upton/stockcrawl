# -*- coding: utf-8 -*-
import scrapy
import json, time, re
from stockcrawl.items import IndustryItem, StockItem

class IndustrySpider(scrapy.Spider):
    name = "industry"
    
    allowed_domains = ["finance.sina.com.cn",
                       "hq.sinajs.cn"
    ]
    
    start_urls = (
        'http://money.finance.sina.com.cn/q/view/newFLJK.php?param=industry',
    )

    varStr = 'var S_Finance_bankuai_industry ='
    varStockStr = 'var hq_str_'
    
    url_stock_list = 'http://hq.sinajs.cn/list=sz399001,'
    url_industry_stocks = 'http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData?page=1&num=100&sort=symbol&asc=1&symbol=&_s_r_a=init&node='
    url_stock = 'http://hq.sinajs.cn/rn=%s&list=%s'

    def parse(self, response):
        body = response.body.decode('gb2312').replace(self.varStr, '')
        industrys = json.loads(body)
        for kk in industrys:
            industry = industrys[kk].split(',')
            item = IndustryItem()
            
            item['code'] = industry[0]
            item['name'] = industry[1]
            item['companys'] = industry[2]
            item['price_avg'] = industry[3]
            item['updn_price'] = industry[4]
            item['updn_per'] = industry[5]
            item['deal_count'] = industry[6]
            item['deal_amount'] = industry[7]
            item['up_num'] = industry[8]
            item['up_per'] = industry[9]
            item['up_current_price'] = industry[10]
            item['up_price'] = industry[11]
            item['up_code'] = industry[12]
            
            url = self.url_industry_stocks + item['code']
            yield scrapy.Request(url, callback=self.industryParse)
            yield item


    def industryParse(self, response):
        body = response.body.decode('gb2312')
        jsonStr = re.sub(r"(,?)([A-Za-z]+?)\s*?:", r"\1'\2':", body).replace("'", "\"");
        stocks = json.loads(jsonStr)
        print body
        i_code = response.url.replace(self.url_industry_stocks, '')
        for stock in stocks:
            symbol = stock['symbol']
            url = self.url_stock % (int(time.time() * 1000), symbol)
            yield scrapy.Request(url, callback=self.stockParse)
            item = StockItem()
            
            item['i_code'] = i_code
            item['code'] = symbol
            item['name'] = stock['name']
            item['trade'] = stock['trade']
            
            
            yield item
            
            
    def stockParse(self, response):
        body = response.body.decode('gb2312')
        body = body.replace(self.varStockStr, '').replace('"', '').replace(';', '')
        
        stockInfo = body.split('=')
        
        item = StockItem()
        item['code'] = stockInfo[0]
        
        stockDetail = stockInfo[1].split(',')
        item['name'] = stockDetail[0]
        
        return [item]
        
        

