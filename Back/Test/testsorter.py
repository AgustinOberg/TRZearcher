import unittest
import csv


class TestSorter(unittest.TestCase):
    search_type = str

    def test_chooses_search_type_correctly(self):
        self.assertEqual(self.__define_search_type(1), "FRASE_EXACTA")
        self.assertEqual(self.__define_search_type(2), "CONTIENE_TODAS_LAS_PALABRAS")
        self.assertEqual(self.__define_search_type(3), "CONTIENE_ALGUNAS_PALABRAS")

    def test_normalizes_price(self):
        self.assertEqual(self.__normalize_price("$21.00"), '$21')

    def test_exports_correctly(self):
        self.search_type = "FRASE_EXACTA"
        self.assertEqual(self.__export(), 'Exportado frase exacta')
        self.search_type = "CONTIENE_TODAS_LAS_PALABRAS"
        self.assertEqual(self.__export(), 'Exportado contiene todas las palabras')
        self.search_type = "CONTIENE_ALGUNAS_PALABRAS"
        self.assertEqual(self.__export(), 'Exportado contiene algunas palabras')

    def test_sort_by_price(self):
        products_list = []
        with open("testpage.csv", 'r') as f:
            file = csv.DictReader(f, delimiter=",")

            for line in file:
                product = [line["Page"], line["Category"].lower(), line["Title"].lower(), int(line["Price"]), line["Link"],
                           line["Time"]]
                products_list.append(product)
        products_list_sorted = products_list.sort(key=lambda e: e[3])
        self.assertEqual(self.__sort_by_price(products_list), products_list_sorted)



    def __sort_by_price(self, products_list):
        products_list.sort(key=lambda e: e[3])
    def __export(self):

        if self.search_type == "FRASE_EXACTA":
            return 'Exportado frase exacta'

        elif self.search_type == "CONTIENE_TODAS_LAS_PALABRAS":
            return 'Exportado contiene todas las palabras'

        elif self.search_type == "CONTIENE_ALGUNAS_PALABRAS":
            return 'Exportado contiene algunas palabras'
    def __normalize_price(self, price):
        price = price.replace('"', "")
        price = price.replace(',', "")
        price = price.replace('.00', "")
        price = price.replace('.', "")
        return price
    def __define_search_type(self,search_type):
        if int(search_type) == 1:
            return "FRASE_EXACTA"
        if int(search_type) == 2:
            return "CONTIENE_TODAS_LAS_PALABRAS"
        if int(search_type) == 3:
            return "CONTIENE_ALGUNAS_PALABRAS"
