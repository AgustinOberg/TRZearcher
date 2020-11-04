import csv
from datetime import datetime
import os

"""
    La clase Export recibe por parametro el producto que estamos buscando, y una lista con listas en cada posicion
     con el formato ["Page", "Category", "Title", "Price", "Link", "Time"] para cada producto de todas las tiendas
    en orden. Esta lista se consigue a traves de la clase Sorter.

"""

class Export:

    def __init__(self, product_to_search, orderded_products):
        self.ordered_products = orderded_products
        self.date = datetime.now()
        self.file_name = str(product_to_search) + "-" + str(self.date.day) + "-" + \
            str(self.date.month) + "-" + str(self.date.year) + ".csv"

    def write(self):
        file = open(os.path.abspath("../../TRZearcher") + "//" + self.file_name, "w", newline='\n')
        with file:
            write = csv.writer(file)
            write.writerow(["Page", "Category", "Title", "Price", "Link", "Time"])
            for product in self.ordered_products:
                write.writerow(product)