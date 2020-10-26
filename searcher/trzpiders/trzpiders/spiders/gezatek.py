import scrapy


class GezatekSpider(scrapy.Spider):
    name = 'gezatek'
    allowed_domains = ['www.gezatek.com.ar']
    start_urls = ['http://www.gezatek.com.ar/']

    def parse(self, response):
        pass
