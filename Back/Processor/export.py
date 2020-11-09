import csv
from datetime import datetime
import os


class Export:

    """
        La clase Export recibe por parametro el producto que estamos buscando, y una lista con listas en cada posicion
         con el formato ["Page", "Category", "Title", "Price", "Link", "Time"] para cada producto de todas las tiendas
        en orden. Esta lista se consigue a traves de la clase Sorter.

    """

    def __init__(self, product_to_search, orderded_products):
        """
        :param product_to_search: String de la busqueda exacta que introdujo el usuario.
        :param orderded_products: Lista de listas que representan productos; deben estar ordenados.
        """
        self.ordered_products = orderded_products
        self.date = datetime.now()
        self.file_name = str(product_to_search) + "-" + str(self.date.day) + "-" + \
            str(self.date.month) + "-" + str(self.date.year) + ".csv"

    def write(self):
        """
        El archivo .csv generado tendrá por nombre la búsqueda y la fecha en que se realizó.
        Escribe los productos que fueron pasados por parámetro en el constructor en él.
        """
        file = open(self.file_name, "w", newline='\n')
        with file:
            write = csv.writer(file)
            write.writerow(["Page", "Category", "Title", "Price", "Link", "Time"])
            for product in self.ordered_products:
                write.writerow(product)
