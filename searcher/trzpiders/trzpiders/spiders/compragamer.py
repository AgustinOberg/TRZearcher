import scrapy
import os
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from scrapy.crawler import CrawlerProcess
from searcher.trzpiders.trzpiders.items import TrzpidersItem

class CompragamerSpider(CrawlSpider):
    """
        Spider que recolecta datos de la pagina www.compragamer.com
    """
    name = 'compragamer' # Nombre de la araña
    custom_settings = {'FEEDS': {'compragamer.csv': {'format': 'csv'}}} # Forma de exportar los datos recolectados
    allowed_domains = ['compragamer.com'] # Dominio que manejamos, del cual no puede salir
    # TODO: Hacer que reciba la palabra a buscar y la reemplace al final
    start_urls = ['https://compragamer.com/index.php?seccion=3&nro_max=800&criterio=nvidia'] # URL donde extraemos los datos
    # Reglas que debera respetar la spider
    rules = {
        # Entra en cada item (para extraer los datos) y luego vuelve a la pagina de extraccion
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//*[@class="products__item"]')),
             callback='parse_item', follow=False)
    }
    # En el caso de existir el archivo, lo elimina
    try:
        os.remove('compragamer.csv')
    except OSError:
        pass

    def parse_item(self, response):
        """
            Recolecta la informacion de cada item
        """
        item = TrzpidersItem()
        item['title'] = str(response.css(
            '.filaNombre div::text').extract_first()).strip()
        item['price'] = str(response.css(
            '.col-xs-5::text').extract_first()).split("$")[1].strip()
        item['category'] = str(response.css(
            '.detalleNombre .product-card__name::text').extract_first()).capitalize().strip()
        item['link'] = str(response.url)
        yield item

    def turn_on_spider(self):
        """
            Enciende el spider
        """
        process = CrawlerProcess({'USER_AGENT': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'})
        process.crawl(CompragamerSpider)
        process.start()