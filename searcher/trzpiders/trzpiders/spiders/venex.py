import scrapy


class VenexSpider(scrapy.Spider):
    name = 'venex'
    allowed_domains = ['www.venex.com.ar']
    start_urls = ['http://www.venex.com.ar/']

    def parse(self, response):
        pass
