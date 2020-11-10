import os
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from Back.Searcher.Config.items import TrzpidersItem
from scrapy.exceptions import CloseSpider
from datetime import datetime


class Fullh4ardSpider(CrawlSpider):
    """
        Spider que recolecta datos de la pagina www.fullh4rd.com.ar, con un limite de 15
    """

    name = 'fullh4ard'

    custom_settings = {'FEEDS': {'fullh4rd.csv': {'format': 'csv'}}}

    allowed_domains = ['www.fullh4rd.com.ar']

    item_count = 0

    url = ""
    filePath = os.path.abspath("../TRZearcher/Back/Searcher/Data/pages_complete.txt")
    with open(filePath, "r") as pages:
        for page in pages:
            if page.find("fullh4rd") > 0:
                url = page

    start_urls = [url]

    rules = {
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//div[@class="item product-list"]')),
             callback='parse_item', follow=False)
    }

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

        item['time'] = (str(datetime.now().year) + "-" + str(datetime.now().month) + "-" + str(
            datetime.now().day) + " " + str(datetime.now().hour) + ":" + str(datetime.now().minute))

        self.item_count += 1
        if self.item_count > 15:
            raise CloseSpider('item exceeded')

        yield item
