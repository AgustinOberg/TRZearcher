import os
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from Back.Searcher.Config.items import TrzpidersItem
from scrapy.exceptions import CloseSpider
from datetime import datetime


class CompragamerSpider(CrawlSpider):
    """
        Spider que recolecta datos de la pagina www.compragamer.com, con un limite de 15
    """

    name = 'compragamer'

    custom_settings = {'FEEDS': {'compragamer.csv': {'format': 'csv'}}}

    allowed_domains = ['compragamer.com']

    item_count = 0

    url = ""
    filePath = os.path.abspath("../TRZearcher/Back/Searcher/Data/pages_complete.txt")
    with open(filePath, "r") as pages:
        for page in pages:
            if page.find("compragamer") > 0:
                url = page

    start_urls = [url]

    rules = {
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//*[@class="products__item"]')),
             callback='parse_item', follow=False)
    }

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

        item['time'] = (str(datetime.now().year) + "-" + str(datetime.now().month) + "-" + str(
            datetime.now().day) + " " + str(datetime.now().hour) + ":" + str(datetime.now().minute))

        self.item_count += 1
        if self.item_count > 15:
            raise CloseSpider('item exceeded')

        yield item
