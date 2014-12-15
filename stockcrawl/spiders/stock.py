# -*- coding: utf-8 -*-
import scrapy


class StockSpider(scrapy.Spider):
    name = "stock"
    allowed_domains = ["finance.sina.com.cn"]
    start_urls = (
    )

    def parse(self, response):
        pass
