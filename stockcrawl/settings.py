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

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'stockcrawl (+http://www.yourdomain.com)'
