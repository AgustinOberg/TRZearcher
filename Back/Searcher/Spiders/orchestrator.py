from Back.Searcher.Spiders.compragamer import CompragamerSpider
from Back.Searcher.Spiders.fullh4rd import Fullh4ardSpider
from Back.Searcher.Spiders.gezatek import GezatekSpider
from Back.Searcher.Spiders.overdrive import OverdriveSpider
from Back.Searcher.Spiders.venex import VenexSpider
from scrapy.crawler import CrawlerProcess


class Orchestrator:

    def execute_spiders(self, titles):
        process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
        })
        if 'compragamer' in titles:
            process.crawl(CompragamerSpider)
        if 'fullh4rd' in titles:
            process.crawl(Fullh4ardSpider)
        if 'gezatek' in titles:
            process.crawl(GezatekSpider)
        if 'overdrive' in titles:
            process.crawl(OverdriveSpider)
        if 'venex' in titles:
            process.crawl(VenexSpider)
        process.start()