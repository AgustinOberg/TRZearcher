import os
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from Back.Searcher.Config.items import TrzpidersItem
from scrapy.exceptions import CloseSpider
from datetime import datetime


class OverdriveSpider(CrawlSpider):
    """
        Spider que recolecta datos de la pagina www.fullh4rd.com.ar, con un limite de 15
    """

    name = 'overdrive'

    custom_settings = {'FEEDS': {'overdrive.csv': {'format': 'csv'}}}

    allowed_domains = ['www.overdrivepc.com.ar']

    item_count = 0

    url = ""
    filePath = os.path.abspath("../TRZearcher/Back/Searcher/Data/pages_complete.txt")
    with open(filePath, "r") as pages:
        for page in pages:
            if page.find("overdrivepc") > 0:
                url = page

    start_urls = [url]

    rules = {
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//a[@class="js-item-link item-link position-absolute w-100"]')),
             callback='parse_item', follow=False)
    }

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

        self.item_count += 1
        if self.item_count > 15:
            raise CloseSpider('item exceeded')

        yield item
