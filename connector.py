import os
import shutil
from searcher.trzpiders.trzpiders.spiders.orchestrator import Orchestrator
from Sorter import Sorter

class Connector:

    def __init__(self, product, compragamer, fullhard, gezatek, venex, overdrive, type_search):
        self.product = product
        self.pages = []
        if (compragamer == 1):
            self.pages.append("compragamer")
        if (fullhard == 1):
            self.pages.append("fullh4rd")
        if (gezatek == 1):
            self.pages.append("gezatek")
        if (venex == 1):
            self.pages.append("venex")
        if (overdrive == 1):
            self.pages.append("overdrive")
        self.__process_product_to_search()
        self.type_search = type_search
        Orchestrator().execute_spiders(self.pages, self.product)
        Sorter(self.pages, self.product, type_search).execute_sorter()

    def __process_product_to_search(self):
        pages_complete = []
        number_of_pages = 0
        with open("pages_initials.txt", "r") as pages_file:
            for page in pages_file:
                number_of_pages += 1
                page = page.rstrip('\n') + self.product + "\n"
                pages_complete.append(page)
        with open("pages_complete.txt", "w") as pages_file:
            for x in range(0, number_of_pages):
                pages_file.write(pages_complete[x])
        shutil.move("pages_complete.txt",
                    ("" + os.getcwd() + "/searcher/trzpiders/trzpiders/spiders/pages_complete.txt"))
        a = open("pages_complete.txt", "w")

