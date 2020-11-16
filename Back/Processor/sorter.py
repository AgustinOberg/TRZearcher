import csv

from Back.Processor.exporter import Exporter
import os

class Sorter:
    """
    Clase que a partir de archivos .csv de cada pagina con toda la informacion que el crawler levanto
    de la web, los lee y organiza en un diccionario el cual esta diseñado para usarse en la clase Export,
    para crear el .csv final.
    """

    def __init__(self, pages_to_search, product_to_search, search_type):
        """
        :param pages_to_search: Lista de Strings con los nombres de las paginas en las que se quiere buscar.
        :param product_to_search: String de la busqueda exacta que introdujo el usuario.
        :param search_type: 1 si se quiere una búsqueda exacta; 2 si se quiere una busqueda que contenga
        todas las palabras; 3 si se quiere una busqueda que contenga algunas palabras.
        """
        self.pages_to_search = pages_to_search
        self.product_to_search = product_to_search.lower()
        self.search_type = self.__define_search_type(search_type)
        self.exact_words = list()
        self.not_exact_words = list()


    def __define_search_type(self, search_type):
        if int(search_type) == 1:
            return "FRASE_EXACTA"
        if int(search_type) == 2:
            return "CONTIENE_TODAS_LAS_PALABRAS"
        if int(search_type) == 3:
            return "CONTIENE_ALGUNAS_PALABRAS"

    def execute_sorter(self):
        self.__read_data()
        self.__sort_by_price(self.exact_words)
        self.__index_dict()
        self.__export()

    def __read_data(self):
        """
        Lee los archivos .csv con categoria, precio, titulo y lo agrega a una lista con cada posicion con
        listas del tipo ["Page", "Category", "Title", "Price", "Link", "Time"]
        """
        for page in self.pages_to_search:
            with open(page + ".csv", 'r', encoding="utf-8") as f:
                file = csv.DictReader(f, delimiter=",")

                for line in file:
                    price = line["price"]
                    price = self.__normalize_price(price)

                    if not self.__has_NoneType(line):
                        product = [page, line["category"].lower(), line["title"].lower(), int(price), line["link"],
                                   line["time"]]
                        if line["title"].lower() == self.product_to_search:
                            self.exact_words.append(product)
                        else:
                            self.not_exact_words.append(product)

    def __has_NoneType(self, line):
        if line["price"] == "None" or line["price"] == "NoneType":
            return True
        elif line["category"] == "None" or line["price"] == "NoneType":
            return True
        elif line["title"] == "None" or line["price"] == "NoneType":
            return True
        elif line["link"] == "None" or line["price"] == "NoneType":
            return True
        elif line["time"] == "None" or line["price"] == "NoneType":
            return True
        else:
            return False

    def __normalize_price(self, price):
        price = price.replace('"', "")
        price = price.replace(',', "")
        price = price.replace('.00', "")
        price = price.replace('.', "")
        return price

    def __export(self):
        """
        Segun el tipo de busqueda elegida, se llamara a una instancia Export con los parametros correspondientes
        para que escriba el .csv con los datos ordenados.
        """

        separated_words = self.product_to_search.split()
        if self.search_type == "FRASE_EXACTA":
            exporter = Exporter(self.product_to_search, self.exact_words)
            self.__write(exporter)

        elif self.search_type == "CONTIENE_TODAS_LAS_PALABRAS":
            products_all_words = self.matching_words_to_product[len(separated_words)]
            self.__sort_by_price(products_all_words)
            products_all_words = self.exact_words + products_all_words
            exporter = Exporter(self.product_to_search, products_all_words)
            self.__write(exporter)

        elif self.search_type == "CONTIENE_ALGUNAS_PALABRAS":
            products_some_words = list()
            self.__collect_products(products_some_words, range(len(separated_words)))
            self.__sort_by_price(products_some_words)
            products_some_words = self.exact_words + products_some_words
            exporter = Exporter(self.product_to_search, products_some_words)
            self.__write(exporter)

    def __write(self, exporter):
        exporter.write_csv()
        exporter.write_html()
        exporter.write_json()

    def __collect_products(self, products_list, amount):
        for x in amount:
            products_list += self.matching_words_to_product[x + 1]

    def __sort_by_price(self, products_list):
        products_list.sort(key=lambda e: e[3])

    def __index_dict(self):
        """
        Crea el diccionario matching_words_to_product el cual indexa con clave de la cantidad de palabras
        que coinciden entre el titulo y lo que se busco. El valor son las listas de productos.

        """
        self.__create_lists_in_dict()
        words = self.product_to_search.split()
        for product in self.not_exact_words:
            separated_title = product[2].split()
            counter = 0
            for word in words:
                if word in separated_title:
                    counter += 1

            self.matching_words_to_product[counter].append(product)

    def __create_lists_in_dict(self):
        """
        Crea listas en cada posicion del diccionario matching_words_to_product
        """
        self.matching_words_to_product = dict()
        words = self.product_to_search.split()
        for x in range(len(words) + 1):
            self.matching_words_to_product[x] = list()
