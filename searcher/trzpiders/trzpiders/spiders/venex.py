
import scrapy
import os
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from scrapy.crawler import CrawlerProcess
from searcher.trzpiders.trzpiders.items import TrzpidersItem

class VenexSpider(CrawlSpider):
    name = 'mercado'
    item_count = 0
    custom_settings = {'FEEDS': {'results.csv': {'format': 'csv'}}}
    allowed_domain = ['www.venex.com.ar']
    start_urls = [
        'https://www.venex.com.ar/resultado-busqueda.htm?keywords=nvidia']

    rules = {
        # Para cada item
        Rule(LinkExtractor(allow=(), restrict_xpaths=(
            '//*[@title=" Anterior "]'))),
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//*[@class="product-box-price clearfix"]')),
             callback='parse_item', follow=False)
    }
    try:
        os.remove('results.csv')
    except OSError:
        pass

    def parse_item(self, response):
        ml_item = TrzpidersItem()
        ml_item['titulo'] = str(response.css(
            '.tituloProducto::text').extract_first()).rstrip('\n').strip()
        ml_item['precio'] = str(response.css(
            '.text-green::text').extract_first()).rstrip('\n').strip()
        ml_item['categoria'] = str(response.css(
            '.headerNavigation+ .headerNavigation::text').extract_first()).rstrip('\n').strip()
        print(ml_item)
        self.item_count += 1
        if self.item_count > 5:
            raise CloseSpider('item_exceeded')
        yield ml_item

    def ejecutar(self):
        process = CrawlerProcess({
            'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
        })
        process.crawl(VenexSpider)
        process.start()

if __name__ == '__main__':
    VenexSpider().ejecutar()