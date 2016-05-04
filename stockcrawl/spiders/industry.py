# -*- coding: utf-8 -*-
import scrapy
import json, time, re, urllib2
from stockcrawl.items import IndustryItem, StockItem

class IndustrySpider(scrapy.Spider):
    name = "industry"
    
    allowed_domains = ["finance.sina.com.cn",
                       "hq.sinajs.cn",
                       "xueqiu.com"
    ]
    
    start_urls = (
        'http://money.finance.sina.com.cn/q/view/newFLJK.php?param=industry',
    )

    varEncode = 'gbk'
    varStr = 'var S_Finance_bankuai_industry ='
    varStockStr = 'var hq_str_'
    
    url_stock_list = 'http://hq.sinajs.cn/list=sz399001,'
    url_industry_stocks = 'http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData?page=1&num=500&sort=symbol&asc=1&symbol=&_s_r_a=init&node='
    url_stock = 'http://xueqiu.com/stock/quote.json?code=%s&_=%s'

    def parse(self, response):
        body = response.body.decode(self.varEncode).replace(self.varStr, '')
        industrys = json.loads(body)
        for kk in industrys:
            industry = industrys[kk].split(',')
            if len(industry[0]) > 0 :
                item = IndustryItem()
                
                item['code'] = industry[0]
                item['name'] = industry[1]
                item['companys'] = industry[2]
                item['price_avg'] = industry[3]
                item['updn_price'] = industry[4]
                item['updn_per'] = industry[5]
                item['up_code'] = industry[12]
                
                url = self.url_industry_stocks + item['code']
                yield scrapy.Request(url, callback=self.industryParse)
                yield item

    def industryParse(self, response):
        body = response.body.decode(self.varEncode)
        jsonStr = re.sub(r"(,?)([A-Za-z]+?)\s*?:", r"\1'\2':", body).replace("'", "\"");
        stocks = json.loads(jsonStr)
        icode = response.url.replace(self.url_industry_stocks, '')
        for stock in stocks:
            symbol = stock['symbol']
            url = self.url_stock % (symbol.upper(), int(time.time() * 1000))
            yield self.stockRequest(url)
            
            item = StockItem()
            
            item['icode'] = icode
            item['code'] = symbol.lower()
            
            yield item
            
            
    def stockRequest(self, url):
        time.sleep(3)
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'    
        headers = {'User-Agent' : user_agent,
                   'Cookie':'s=5ru12a2oaf; xq_a_token=76dc94e5dabad0982db9673532f78492a47f0bb1; xqat=76dc94e5dabad0982db9673532f78492a47f0bb1; xq_r_token=b3fd6591326685236a0d6deaeab6d01108df2af8; xq_token_expire=Sat%20May%2021%202016%2015%3A22%3A13%20GMT%2B0800%20(CST); xq_is_login=1; u=2507362198; bid=60b8d8964a3b13c38655dc881d732ede_inh3uhfw; webp=1; Hm_lvt_1db88642e346389874251b5a1eded6e3=1461655304; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1462338105; __utmt=1; __utma=1.989006370.1453429847.1461655611.1462338105.7; __utmb=1.1.10.1462338105; __utmc=1; __utmz=1.1458712787.4.4.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)'
        }
          
        req = urllib2.Request(url, None, headers)    
        response = urllib2.urlopen(req)  
        body = response.read()
        
        if response.getcode() == 200:
            data = json.loads(body)
            quotes = data.get('quotes')
            if quotes :
                if len(quotes) > 0:
                    stock = quotes[0]
                    item = StockItem()
                    item['code'] = stock['symbol'].lower()               
                    item['name'] = stock['name']
                    item['price'] = stock['current']
                    item['totalShares'] = stock['totalShares']  # 总股本：122.60亿
                    item['float_shares'] = stock['float_shares']  # 流通股本：101.26亿
                    item['eps'] = stock['eps']  # 每股收益：0.35
                    item['dividend'] = stock['dividend']  # 每股股息：0.20
                    item['net_assets'] = stock['net_assets']  # 每股净资产：3.87
                    item['pe_lyr'] = stock['pe_lyr']  # 市盈率LYR：40.88
                    item['pe_ttm'] = stock['pe_ttm']  # 市盈率TTM：30.32
                    item['pb'] = stock['pb']  # 市净率TTM：3.64
                    item['psr'] = stock['psr']  # 市销率TTM：1.62
                    
                    return item
                
        return None
        
