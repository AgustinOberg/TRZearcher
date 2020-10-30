import os
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from searcher.trzpiders.trzpiders.items import TrzpidersItem
from datetime import datetime

class VenexSpider(CrawlSpider):
    """
        Spider que recolecta datos de la pagina www.venex.com.ar
    """

    name = 'venex' # Nombre de la araña

    custom_settings = {'FEEDS': {'venex.csv': {'format': 'csv'}}} # Forma de exportar los datos recolectados

    allowed_domain = ['www.venex.com.ar'] # Dominio que manejamos, del cual no puede salir

    # Buscamos la url completa
    url = ""
    with open("pages_complete.txt", "r") as pages:
        for page in pages:
            if page.find("venex") > 0:
                url = page

    start_urls = [url] # URL donde extraemos los datos

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

        item['time'] = (str(datetime.now().year) + "-" + str(datetime.now().month) + "-" + str(
            datetime.now().day) + " " + str(datetime.now().hour) + ":" + str(datetime.now().minute))

        yield item