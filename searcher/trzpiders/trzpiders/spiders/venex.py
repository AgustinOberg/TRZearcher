import scrapy
import os
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from scrapy.crawler import CrawlerProcess
from trzpiders.items import TrzpidersItem


class VenexSpider(CrawlSpider):
    """
        Spider que recolecta datos de la pagina www.venex.com.ar
    """
    name = 'venex' # Nombre de la araña
    custom_settings = {'FEEDS': {'venex.csv': {'format': 'csv'}}} # Forma de exportar los datos recolectados
    allowed_domain = ['www.venex.com.ar'] # Dominio que manejamos, del cual no puede salir
    # TODO: Hacer que reciba la palabra a buscar y la reemplace al final
    start_urls = ['https://www.venex.com.ar/resultado-busqueda.htm?keywords=nvidia'] # URL donde extraemos los datos
    # Reglas que debera respetar la spider
    rules = {
        # En el caso de haber pagina siguiente
        Rule(LinkExtractor(allow=(), restrict_xpaths=(
            '//*[@title=" Anterior "]'))),
        # Entra en cada item (para extraer los datos) y luego vuelve a la pagina de extraccion
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//*[@class="product-box-price clearfix"]')),
             callback='parse_item', follow=False)
    }

    # En el caso de existir el archivo, lo elimina
    try:
        os.remove('venex.csv')
    except OSError:
        pass


    def parse_item(self, response):
        """
            Recolecta la informacion de cada item
        """
        item = TrzpidersItem()
        item['title'] = str(response.css(
            '.tituloProducto::text').extract_first()).strip()
        item['price'] = str(response.css(
            '.text-green::text').extract_first()).strip().split("$")[1]
        item['category'] = str(response.css(
            '.headerNavigation+ .headerNavigation::text').extract_first()).capitalize().strip()
        item['link'] = str(response.url)
        yield item

    def turn_on_spider(self):
        """
            Enciende el spider
        """
        process = CrawlerProcess(
            {'USER_AGENT': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'})
        process.crawl(VenexSpider)
        process.start()
        
if __name__ == "__main__":
    VenexSpider().turn_on_spider()