import scrapy


class CompragamerSpider(scrapy.Spider):
    name = 'compragamer'
    allowed_domains = ['compragamer.com']
    start_urls = ['http://compragamer.com/']

    def parse(self, response):
        pass
