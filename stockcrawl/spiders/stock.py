# -*- coding: utf-8 -*-
import scrapy


class StockSpider(scrapy.Spider):
    name = "stock"
    allowed_domains = ["finance.sina.com.cn"]
    start_urls = (
        'http://www.finance.sina.com.cn/',
    )

    def parse(self, response):
        pass
