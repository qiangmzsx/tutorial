# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.http import  Request
from tutorial.doubanItems import  DoubanItem 

class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["douban.com"]
    start_urls = (
        'http://movie.douban.com/top250',
    )
    page_url = 'http://movie.douban.com/top250'
    def parse(self, response):
        item = DoubanItem()
        print '======================'
        content = response.xpath('//div[@class="info"]')
        for info in content:
            hd = info.xpath('div[@class="hd"]/a/span/text()').extract()
            item['title'] = ";".join(hd).replace('\n','').replace(' ','')
            item['messages'] = info.xpath('div[@class="bd"]/p/text()').extract()[0].replace('\n','').replace(' ','')
            bd = info.xpath('div[@class="bd"]')
            #item['star'] = bd.xpath('div[@class="star"]/span[@class="rating_num"]/text()').extract()
            item['star'] = bd.xpath('div/span/text()').extract()[0]
            item['assess'] = re.findall('(\d+)', bd.xpath('div/span/text()').extract()[1], re.S)
            print '=========='+str(item)+'============'
            yield item #一定要有
            
        nextLink = response.xpath('//span[@class="next"]/a/@href').extract()
        if nextLink:
           nextLink = nextLink[0]
           print nextLink
           yield Request(self.page_url+ nextLink,callback=self.parse) 
        
