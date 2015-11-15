import scrapy

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://blog.csdn.net/liyuetao680/article/details/48313313",
        #"http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        print filename
        with open(filename, 'wb') as f:
            f.write(response.body)   