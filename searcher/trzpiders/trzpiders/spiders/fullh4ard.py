import scrapy


class Fullh4ardSpider(scrapy.Spider):
    name = 'fullh4ard'
    allowed_domains = ['www.fullh4rd.com.ar']
    start_urls = ['http://www.fullh4rd.com.ar/']

    def parse(self, response):
        pass
