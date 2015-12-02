# -*- coding: utf-8 -*-
import scrapy
from tutorial.stockQQItems import StockQQItem
from scrapy.http import  Request

class StockqqSpider(scrapy.Spider):
    name = "StockQQ"
    allowed_domains = ["stock.qq.com"]
    start_urls = (
        'http://stock.qq.com/l/stock/list20150525114649.htm',
    )
    #先获取所有的分页
    #获取每一个分页列表中的文章url
    #解析文章数据
    def parse(self, response):
        print '@@@@@@@@@@@@@@@@@@'
        req = []
        nextLink = response.xpath('//div[@class="pageNav"]/a[@class="f12"]/@href').extract()
        if nextLink:
            if len(nextLink)>3:
                nextLink = nextLink[1]
            elif  len(nextLink)>=0:
                nextLink = nextLink[0]
            r =  Request(nextLink,callback=self.parse_list,dont_filter=True)#dont_filter=True表示不过滤相同url
            print '***********************'+nextLink
            n = Request(nextLink,callback=self.parse,dont_filter=True)
            req.append(n)
            req.append(r)
            print '####################'
            
        return req 
        
    
    #获取每一个分页列表中的文章url
    def parse_list(self,response):
        print "=============="
        req = []
        item = StockQQItem()
        item['pageLink'] = response.url
        listTitles = response.xpath('//div[@class="mod newslist"]/ul') 
        for titleul in listTitles:
            listLis = titleul.xpath('li')
            #详细内容
            for li in listLis:
                titleLink = li.xpath('a/@href').extract()
                print str(titleLink)
                r= Request(titleLink[0], callback=self.parse_content)
                r.meta['item'] = item
                req.append(r)
                
        return req
    
    def parse_content(self,response):
        print "+++++++++++++++++"
        item = response.meta['item']
        comtentDiv = response.xpath('//*[@id="C-Main-Article-QQ"]')
        item['title'] = comtentDiv.xpath('div[@class="hd"]/h1/text()').extract()
        item['tag'] = comtentDiv.xpath('div/div[@bosszone="titleDown"]/div[@class="l1"]/span[@bosszone="ztTopic"]/a/text()').extract()[0]
        
        source = comtentDiv.xpath('div/div[@bosszone="titleDown"]/div[@class="l1"]/span[@bosszone="jgname"]/text()').extract()
        if len(source)>0:
            item['source'] =source[0]
        else : 
            item['source'] = comtentDiv.xpath('div/div[@bosszone="titleDown"]/div[@class="l1"]/span[@bosszone="jgname"]/a/text()').extract()
        
        item['articleTime'] = comtentDiv.xpath('div/div[@bosszone="titleDown"]/div[@class="l1"]/span[@class="pubTime article-time"]/text()').extract()[0]
        comtents = response.xpath('//*[@id="Cnt-Main-Article-QQ"]/p/text()').extract()
        strComtent = ''
        for comtent in comtents:
            strComtent += comtent
        
        item['comtent'] = strComtent
        item['link'] = response.url
        return item 

        
        
        
        
        
        