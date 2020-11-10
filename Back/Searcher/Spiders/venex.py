import os
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from Back.Searcher.Config.items import TrzpidersItem
from scrapy.exceptions import CloseSpider
from datetime import datetime


class VenexSpider(CrawlSpider):
    """
        Spider que recolecta datos de la pagina www.venex.com.ar, con un limite de 15
    """

    name = 'venex'

    custom_settings = {'FEEDS': {'venex.csv': {'format': 'csv'}}}

    allowed_domain = ['www.venex.com.ar']

    item_count = 0

    url = ""
    filePath = os.path.abspath("../TRZearcher/Back/Searcher/Data/pages_complete.txt")
    with open(filePath, "r") as pages:
        for page in pages:
            if page.find("venex") > 0:
                url = page

    start_urls = [url]

    rules = {
        Rule(LinkExtractor(allow=(), restrict_xpaths=(
            '//*[@title=" Anterior "]'))),

        Rule(LinkExtractor(allow=(), restrict_xpaths=('//*[@class="product-box-price clearfix"]')),
             callback='parse_item', follow=False)
    }

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

        self.item_count += 1
        if self.item_count > 15:
            raise CloseSpider('item exceeded')

        yield item
