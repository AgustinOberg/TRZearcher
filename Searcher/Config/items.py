import scrapy

class TrzpidersItem(scrapy.Item):
    """
        Define que items vamos a recolectar con nuestro Scrapy
    """
    title = scrapy.Field()
    price = scrapy.Field()
    category = scrapy.Field()
    link = scrapy.Field()
    time = scrapy.Field()