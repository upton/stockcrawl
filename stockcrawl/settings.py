# -*- coding: utf-8 -*-

# Scrapy settings for stockcrawl project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
BOT_NAME = 'stockcrawl'

SPIDER_MODULES = ['stockcrawl.spiders']
NEWSPIDER_MODULE = 'stockcrawl.spiders'

ITEM_PIPELINES = ['stockcrawl.pipelines.StockcrawlPipeline']

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
CONCURRENT_ITEMS = 1
DOWNLOAD_DELAY = 3
LOG_LEVEL = 'INFO'