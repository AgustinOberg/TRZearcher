import os
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from searcher.trzpiders.trzpiders.items import TrzpidersItem
from datetime import datetime

class OverdriveSpider(CrawlSpider):
    """
        Spider que recolecta datos de la pagina www.fullh4rd.com.ar
    """

    name = 'overdrive' # Nombre de la araña

    custom_settings = {'FEEDS': {'overdrive.csv': {'format': 'csv'}}} # Forma de exportar los datos recolectados

    allowed_domains = ['www.overdrivepc.com.ar'] # Dominio que manejamos, del cual no puede salir

    # Buscamos la url completa
    url = ""
    with open("pages_complete.txt", "r") as pages:
        for page in pages:
            if page.find("overdrivepc") > 0:
                url = page

    start_urls = [url] # URL donde extraemos los datos

    # Reglas que debera respetar la spider
    rules = {
        # Entra en cada item (para extraer los datos) y luego vuelve a la pagina de extraccion
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//a[@class="js-item-link item-link position-absolute w-100"]')),
             callback='parse_item', follow=False)
    }

    # En el caso de existir el archivo, lo elimina
    try:
        os.remove('overdrive.csv')
    except OSError:
        pass

    def parse_item(self, response):
        """
            Recolecta la informacion de cada item
        """
        item = TrzpidersItem()

        item['title'] = str(response.css(
            '#product-name::text').extract_first()).lower().capitalize().rstrip('\n').strip()

        item['price'] = str(response.css(
            '#price_display::text').extract_first()).rstrip('\n').strip().split("$")[1]

        item['category'] = str(response.css(
            '.crumb:nth-child(5)::text').extract()).capitalize().strip()[2:-2]

        item['link'] = str(response.url)

        item['time'] = (str(datetime.now().year) + "-" + str(datetime.now().month) + "-" + str(
            datetime.now().day) + " " + str(datetime.now().hour) + ":" + str(datetime.now().minute))

        yield item