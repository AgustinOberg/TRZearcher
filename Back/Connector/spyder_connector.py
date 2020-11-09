from Back.Searcher.Spiders.orchestrator import Orchestrator
from Back.Processor.sorter import Sorter
import os


class Connector:

    def __init__(self, product, compragamer, fullhard, gezatek, venex, overdrive, type_search):
        self.product = product
        self.pages = []
        if int(compragamer) == 1:
            self.pages.append("compragamer")
        if int(fullhard) == 1:
            self.pages.append("fullh4rd")
        if int(gezatek) == 1:
            self.pages.append("gezatek")
        if int(overdrive) == 1:
            self.pages.append("overdrive")
        if int(venex) == 1:
            self.pages.append("venex")
        self.type_search = type_search
        print(self.pages)
        Orchestrator().execute_spiders(self.pages)
        Sorter(self.pages, self.product, type_search).execute_sorter()
        self.__clean()

    def __clean(self):
        os.remove("./Back/Connector/temp_connector.txt")
        os.remove("compragamer.csv")
        os.remove("fullh4rd.csv")
        os.remove("gezatek.csv")
        os.remove("overdrive.csv")
        os.remove("venex.csv")