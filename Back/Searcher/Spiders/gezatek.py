import os
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from Back.Searcher.Config.items import TrzpidersItem
from scrapy.exceptions import CloseSpider
from datetime import datetime


class GezatekSpider(CrawlSpider):
    """
        Spider que recolecta datos de la pagina www.gezatek.com.ar, con un limite de 15
    """

    name = 'gezatek'

    custom_settings = {'FEEDS': {'gezatek.csv': {'format': 'csv'}}}

    allowed_domains = ['www.gezatek.com.ar']

    item_count = 0

    url = ""
    filePath = os.path.abspath("../TRZearcher/Back/Searcher/Data/pages_complete.txt")
    with open(filePath, "r") as pages:
        for page in pages:
            if page.find("gezatek") > 0:
                url = page

    start_urls = [url]

    rules = {
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//div[@class="w-box product "]')),
             callback='parse_item', follow=False)
    }

    try:
        os.remove('gezatek.csv')
    except OSError:
        pass

    def parse_item(self, response):
        """
            Recolecta la informacion de cada item
        """

        item = TrzpidersItem()

        item['title'] = str(response.css(
            '.nombre h3::text').extract_first()).strip()

        item['price'] = str(response.css(
            '.precio_web h7::text').extract_first()).strip()

        item['category'] = str(response.css(
            '.col-md-5 h7::text').extract_first()).capitalize().strip()

        item['link'] = str(response.url)

        item['time'] = (str(datetime.now().year) + "-" + str(datetime.now().month) + "-" + str(
            datetime.now().day) + " " + str(datetime.now().hour) + ":" + str(datetime.now().minute))

        self.item_count += 1
        if self.item_count > 15:
            raise CloseSpider('item exceeded')

        yield item
