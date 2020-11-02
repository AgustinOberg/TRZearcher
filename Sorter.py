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
        self.exact_words = list()
        self.some_words = list()
        self.products = list()
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

        #category,link,price,time,title
        for page in self.pages_to_search:
                with open("searcher/trzpiders/trzpiders/spiders/"+page+".csv", 'r', encoding="utf-8") as f:
                    file = csv.DictReader(f, delimiter=",")

                    for line in file:
                        price = line["price"].replace('"',"")
                        price = price.replace(',',"")
                        price= price.replace('.00',"")

                        product = [page,line["category"], line["title"], int(price), line["link"],line["time"]]
                        if line["title"] == self.product_to_search:
                            self.exact_words.append(product)
                        else:
                            self.some_words.append(product)

        self.exact_words.sort(key=lambda e: e[3])
        self.some_words.sort(key=lambda e: e[3])
        self.products = self.exact_words + self.some_words


    def export(self):
      Export(self.product_to_search, self.dictionary).write()
