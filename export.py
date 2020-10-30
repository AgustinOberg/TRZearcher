import csv
import os
from datetime import datetime

"""
    La clase Export recibe por parametro el producto que estamos buscando, y un diccionario con el formato {Pagina : [ [Producto , Precio], [Producto , Precio] ] }

"""


class Export:

    # TODO: La informacion debe venir ordenada
    def __init__(self, product_to_search, orderded_products):
        self.__ordered_products = orderded_products
        self.date = datetime.now()
        self.__file_name = str(product_to_search) + "-" + str(self.date.day) + "-" + \
            str(self.date.month) + "-" + str(self.date.year) + ".csv"
        #category,link,price,time,title

    def write(self):
        file = open(self.__file_name, "w", newline='\n')
        with file:
            write = csv.writer(file)
            for product in self.__ordered_products:
                write.writerow(product)