# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import XiciItem

class XiciSpider(scrapy.Spider):
    name = 'Xici'
    allowed_domains = ['xicidaili.com']
    start_urls = (
        'http://www.xicidaili.com/',
    )

    def start_requests(self):
        reqs = []
        
        for i in range (1,3):
            rep = scrapy.Request('http://www.xicidaili.com/nn/%s'%i)
            reqs.append(rep)
        
        return reqs
    
    def parse(self, response):
        ip_list = response.xpath('//*[@id="ip_list"]')#("/html/body/div[1]/div[2]/table")
        
        trs = ip_list[0].xpath('tr')
        print '=========================='
        print len(trs)
        items = []
        for ip in trs[1:]:
            pre_item = XiciItem()
            td = ip.xpath('td')
            pre_item['IP'] = ip.xpath('td/text()')[0].extract()
            pre_item['PORT'] = ip.xpath('td/text()')[1].extract()
            pre_item['TYPE'] = ip.xpath('td/text()')[5].extract()
            pre_item['PORITION'] =  td[4].xpath('a/text()').extract()
            pre_item['LAST_CHECK_TIME'] = ip.xpath('td/text()')[9].extract()#td[9].extract()
            pre_item['SPEED'] =td[8].xpath('div/@title')[0].extract()
            # img =  td[1].xpath('//@src').extract()
#             pre_item['IP'] =  ip.xpath('td/text()')[0].extract()
#             pre_item['PORT'] = ip.xpath('td/text()')[1].extract()
#             pre_item['PORITION'] = ip.xpath('td/text()')[4].extract()
#             pre_item['TYPE'] = ip.xpath('td/text()')[5].extract()
            #pre_item['SPEED'] =ip.xpath('td/text()')[4].extract()
            #pre_item['LAST_CHECK_TIME'] = ip.xpath('td/text()')[10].extract()
            items.append(pre_item)
            
        return items 
