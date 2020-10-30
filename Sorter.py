import csv

from export import Export


class Sorter:
    """
    Clase que a partir de archivos .csv de cada pagina con toda la informacion que el crawler levanto
    de la web, los lee y organiza en un diccionario el cual esta diseñado para usarse en la clase Export,
    para crear el .csv final.
    """


    def __init__(self, pages_to_search, product_to_search):
        self.pages_to_search = pages_to_search
        self.product_to_search = product_to_search
        self.dictionary = dict()
        self.exact_words = list()
        self.some_words = list()
        self.read_and_sort()
        self.export()

    #Falta recuperar categoria, link de la publicacion, fecha-hora
    def read_and_sort(self):
        """
        Lee los archivos .csv con categoria, precio, titulo y lo agrega a un diccionario con
        key: pagina value: [[titulo,precio],...].
        Este diccionario esta ordenado, primeramente por exactitud de la frase que se quiere buscar,
        y en segundo lugar por el precio mas economico.
        """
        for page in super.get_pages_to_search():
                with open(page+".csv", 'r', encoding="utf-8") as f:
                    file = csv.DictReader(f, delimiter=",")

                    for line in file:
                        product = [line["titulo"], int(line["precio"][1:])]
                        if line["titulo"] == self.product_to_search:
                            self.exact_words.append(product)
                        else:
                            self.some_words.append(product)
                self.exact_words.sort(key = lambda e: e[1])
                self.some_words.sort(key = lambda e: e[1])
                products = self.exact_words + self.some_words
                self.dictionary[page] = products

    def export(self):
        Export(self.product_to_search, self.dictionary).write()
