import scrapy
import os
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from scrapy.crawler import CrawlerProcess
from searcher.trzpiders.trzpiders.items import TrzpidersItem

class Fullh4ardSpider(CrawlSpider):
    """
        Spider que recolecta datos de la pagina www.fullh4rd.com.ar
    """
    name = 'fullh4ard' # Nombre de la araña
    custom_settings = {'FEEDS': {'fullh4rd.csv': {'format': 'csv'}}} # Forma de exportar los datos recolectados
    allowed_domains = ['www.fullh4rd.com.ar'] # Dominio que manejamos, del cual no puede salir
    # TODO: Hacer que reciba la palabra a buscar y la reemplace al final
    start_urls = ['https://www.fullh4rd.com.ar/cat/search/auricular'] # URL donde extraemos los datos
    # Reglas que debera respetar la spider
    rules = {
        # Entra en cada item (para extraer los datos) y luego vuelve a la pagina de extraccion
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//div[@class="item product-list"]')),
             callback='parse_item', follow=False)
    }
    # En el caso de existir el archivo, lo elimina
    try:
        os.remove('fullh4rd.csv')
    except OSError:
        pass

    def parse_item(self, response):
        """
            Recolecta la informacion de cada item
        """
        item = TrzpidersItem()
        item['title'] = str(response.css(
            'h1::text').extract_first()).lower().capitalize().rstrip('\n').strip()
        item['price'] = str(response.css(
            '.price-main::text').extract_first()).rstrip('\n').strip().split("$")[1]
        item['category'] = str(response.css(
            'a:nth-child(3) span::text').extract()[2]).capitalize().strip()
        item['link'] = str(response.url)
        yield item

    def turn_on_spider(self):
        """
            Enciende el spider
        """
        process = CrawlerProcess({'USER_AGENT': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'})
        process.crawl(Fullh4ardSpider)
        process.start()