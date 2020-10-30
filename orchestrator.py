from searcher.trzpiders.trzpiders.spiders.compragamer import CompragamerSpider
from searcher.trzpiders.trzpiders.spiders.fullh4ard import Fullh4ardSpider
from searcher.trzpiders.trzpiders.spiders.gezatek import GezatekSpider
from searcher.trzpiders.trzpiders.spiders.venex import VenexSpider
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
from Sorter import Sorter


class Orchestrator:
    def __init__(self, titles,product):
        self.titles= titles
        self.process = CrawlerProcess(get_project_settings())
        self.__init_spiders()
        self.export = Sorter(titles,product)
        print("Programa finalizado")
        
    def __init_spiders(self):
        for title in self.titles:
            if title == 'Compra Gamer':
                self.process.crawl(CompragamerSpider)
            elif title== 'Gezatek':
                self.process.crawl(GezatekSpider)
            elif title == 'Venex':
                self.process.crawl(VenexSpider)
            elif title == 'Full H4rd':
                self.process.crawl(Fullh4ardSpider)
        self.process.start()