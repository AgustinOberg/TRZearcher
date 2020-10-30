from searcher.trzpiders.trzpiders.spiders.compragamer import CompragamerSpider
from searcher.trzpiders.trzpiders.spiders.fullh4ard import Fullh4ardSpider
from searcher.trzpiders.trzpiders.spiders.gezatek import GezatekSpider
from searcher.trzpiders.trzpiders.spiders.venex import VenexSpider
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess

class Orchestrator:

    def execute_spiders(self, titles, product):
        process = CrawlerProcess(get_project_settings())
        if 'Compra Gamer' in titles:
            process.crawl(CompragamerSpider)
        if 'Full H4rd' in titles:
            process.crawl(Fullh4ardSpider)
        if 'Gezatek'in titles:
            process.crawl(GezatekSpider)
        if 'Venex' in titles:
            process.crawl(VenexSpider)
        process.start()
