import os
import shutil
from searcher.trzpiders.trzpiders.spiders.orchestrator import Orchestrator
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess


class Interface:

    def __init__(self):
        self.pages = ["Compra Gamer", "Gezatek", "Venex", "Full H4rd"]
        self.active_pages = []
        self.pages_to_search = self.__reader()
        self.search_type = 1
        self.__message_product_to_search()
        self.__message_pages_to_search()
        self.__message_search_type()
        self.__process_product_to_search()
        #Orchestrator().execute_spiders(self.pages, self.product)

    def __message_product_to_search(self):
        self.product = input("***************************************************************"
                             + "\n"
                             + "\n                     CHOOGLE"
                             + "\n                       TRZ"
                             + "\n"
                             + "\n Somos un buscador/comparador de precios de productos GAMERS"
                             + "\n"
                             + "\n Introduzca el producto a buscar: ")

    def __message_pages_to_search(self):
        print("\n***************************************************************"
              + "\n"
              + "\n Responder con un si en el caso de querer incluirla")
        i = 0
        for page in self.pages:
            boolean = input(
                "\n Quieres incluir en tu comparacion a " + str(page) + "? ")
            if boolean.lower() == "si":
                self.active_pages.append(self.pages_to_search[i])
                i += 1

    def __message_search_type(self):
        self.search_type = input("\n ¿ Que tipo de busqueda quieres realizar ?"
                                 + "\n"
                                 + "\n 1 - Publicación con la frase exacta"
                                 + "\n 2 - Publicación que contenga todas las palabras"
                                 + "\n 3 - Publicación que contenga algunas de las palabras"
                                 + "\n"
                                 + "\n ")

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

    def __reader(self):
        with open("pages_initials.txt", 'r') as pages_file:
            pages = list(map(str.rstrip, pages_file))
        return pages
