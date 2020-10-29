from searcher.trzpiders.trzpiders.spiders.compragamer import CompragamerSpider
from searcher.trzpiders.trzpiders.spiders.fullh4ard import Fullh4ardSpider
from searcher.trzpiders.trzpiders.spiders.gezatek import GezatekSpider
from searcher.trzpiders.trzpiders.spiders.venex import VenexSpider
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess

class Ejecutor:

    def ejecutar(self):
        process = CrawlerProcess(get_project_settings())
        process.crawl(CompragamerSpider)
        process.crawl(Fullh4ardSpider)
        process.crawl(GezatekSpider)
        process.crawl(VenexSpider)
        process.start()

if __name__ == '__main__':
    Ejecutor().ejecutar()
