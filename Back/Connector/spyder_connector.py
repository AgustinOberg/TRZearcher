from Back.Searcher.Spiders.orchestrator import Orchestrator
from Back.Processor.sorter import Sorter
import os
import sys

class Connector:

    def __init__(self, product, compragamer, fullhard, gezatek, venex, overdrive, type_search):
        self.product = product
        self.pages = self.__spiders_validation(compragamer, fullhard, gezatek, venex, overdrive)
        self.type_search = type_search

    def __spiders_validation(self, compragamer, fullhard, gezatek, venex, overdrive):
        pages = []
        if int(compragamer) == 1:
            pages.append("compragamer")
        if int(fullhard) == 1:
            pages.append("fullh4rd")
        if int(gezatek) == 1:
            pages.append("gezatek")
        if int(overdrive) == 1:
            pages.append("overdrive")
        if int(venex) == 1:
            pages.append("venex")
        return pages

    def execute_connector(self):
        Orchestrator().execute_spiders(self.pages)
        Sorter(self.pages, self.product, self.type_search).execute_sorter()
        self.__clean()
        sys.exit()

    def __clean(self):
        os.remove("./Back/Connector/temp_connector.txt")
        os.remove("./Back/Searcher/Data/pages_complete.txt")
        for page in self.pages:
            os.remove(page + ".csv")