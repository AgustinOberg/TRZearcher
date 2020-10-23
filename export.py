import csv
import os

"""
    La clase Export recibe por parametro el producto que estamos buscando, y un diccionario con el formato {Pagina : [ [Producto , Precio], [Producto , Precio] ] }

"""


class Export:

    def __init__(self, product_to_search, page_product_price):
        self.__page_product_price = page_product_price
        self.__file_name = "Comparate - " + str(product_to_search) + ".csv"
        self.__header = ("Page", "Product", "Price")
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
