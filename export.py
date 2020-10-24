import csv
import os
from datetime import datetime

"""
    La clase Export recibe por parametro el producto que estamos buscando, y un diccionario con el formato {Pagina : [ [Producto , Precio], [Producto , Precio] ] }

"""


class Export:

    # TODO: La informacion debe venir ordenada
    def __init__(self, product_to_search, page_product_price):
        self.__page_product_price = page_product_price
        self.date = datetime.now()
        self.__file_name = str(product_to_search) + "-" + str(self.date.day) + "-" + \
            str(self.date.month) + "-" + str(self.date.year) + ".csv"
        self.__header = ("Page", "Product", "Price")
        # TODO: Agregar categoria, link de la publicacion, fecha-hora
        self.__write_header()

    def __write_header(self):
        with open(self.__file_name, "w", newline='') as file:
            writer = csv.DictWriter(
                file, fieldnames=self.__header, delimiter=";")
            writer.writeheader()

    def __write(self, **data):
        with open(self.__file_name, "a", newline='') as file:
            writer = csv.DictWriter(
                file, fieldnames=self.__header, delimiter=";")
            writer.writerow(data)

    def write(self):
        """
            Escribe en un csv con los datos recibidos

        """
        for page, product_price in self.__page_product_price.items():
            for product in product_price:
                self.__write(Page=str(page), Product=str(
                    product[0]), Price=str(product[1]))


if __name__ == "__main__":
    dic = {"CompraGamer": [["Nvidia RTX 2080", "70000"], [
        "Nvidia RTX 2080 TI", "90000"]], "Venex": [["Nvidia RTX 2080 TI", "95000"]]}
    Export("Nvidia RTX 2080", dic).write()
