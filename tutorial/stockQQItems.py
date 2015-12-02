# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class StockQQItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    comtent = scrapy.Field()
    source = scrapy.Field()
    articleTime = scrapy.Field()
    tag = scrapy.Field()
    link = scrapy.Field()
    pageLink = scrapy.Field()
