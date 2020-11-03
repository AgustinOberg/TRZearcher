import csv

from export import Export


class Sorter:
    """
    Clase que a partir de archivos .csv de cada pagina con toda la informacion que el crawler levanto
    de la web, los lee y organiza en un diccionario el cual esta diseñado para usarse en la clase Export,
    para crear el .csv final.
    """

    def __init__(self, pages_to_search, product_to_search, search_tipe):
        self.pages_to_search = pages_to_search
        self.product_to_search = product_to_search.title()
        self.search_tipe = search_tipe
        self.exact_words = list()
        self.not_exact_words = list()
        self.read_and_sort()
        self.export()

    def read_and_sort(self):
        """
        Lee los archivos .csv con categoria, precio, titulo y lo agrega a una lista con cada posicion con
        listas del tipo ["Page", "Category", "Title", "Price", "Link", "Time"]
        Esta lista esta ordenado, primeramente por exactitud de la frase que se quiere buscar,
        y en segundo lugar por el precio mas economico.
        """

        for page in self.pages_to_search:
                with open("searcher/trzpiders/trzpiders/spiders/"+page+".csv", 'r', encoding="utf-8") as f:
                    file = csv.DictReader(f, delimiter=",")

                    for line in file:
                        price = line["price"].replace('"',"")
                        price = price.replace(',',"")
                        price= price.replace('.00',"")

                        product = [page,line["category"].title(), line["title"].title(), int(price), line["link"],line["time"]]
                        if line["title"] == self.product_to_search:
                            self.exact_words.append(product)
                        else:
                            self.not_exact_words.append(product)

        self.exact_words.sort(key=lambda e: e[3])


    def export(self):
        """
        Usa el atributo search_tipe que contiene alguna de estas 3 posibilidades de tipo de busqueda:
        1 - Publicación con la frase exacta"
        2 - Publicación que contenga todas las palabras"
        3 - Publicación que contenga algunas de las palabras"

        Segun la elegida, se llamara a una instancia Export con los parametros correspondientes
        """
        self.__dict_n_coincidences_to_products()
        words = self.product_to_search.split()
        if(self.search_tipe == 1):
            Export(self.product_to_search, self.exact_words).write()

        elif(self.search_tipe == 2):
            products_all_words = self.matching_words_to_product[len(words)]
            products_all_words.sort(key=lambda e: e[3])
            products_all_words = self.exact_words + products_all_words
            Export(self.product_to_search, products_all_words).write()

        elif(self.search_tipe == 3):
            products_some_words = list()
            for x in range(len(words)):
                products_some_words += self.matching_words_to_product[x+1]
            products_some_words.sort(key=lambda e: e[3])
            products_some_words = self.exact_words + products_some_words
            Export(self.product_to_search, products_some_words).write()


    def __dict_n_coincidences_to_products(self):
        """
        crea el atributo matching_words_to_product el cual es un diccionario con clave de la cantidad de palabras
        que coinciden entre el titulo y lo que se busco. El valor son las listas de productos.

        """
        self.create_lists_in_dict()
        words = self.product_to_search.split()
        for product in self.not_exact_words:
            separated_title = product[2].split()
            counter = 0
            for word in words:
                if word in separated_title:
                    counter += 1

            self.matching_words_to_product[counter].append(product)

    def create_lists_in_dict(self):
        """
        Crea listas en cada posicion del diccionario matching_words_to_product
        """
        self.matching_words_to_product = dict()
        words = self.product_to_search.split()
        for x in range(len(words)+1):
            self.matching_words_to_product[x] = list()

if __name__ == '__main__':
    pages = ['compragamer', 'fullh4rd', 'gezatek', 'venex']
    Sorter(pages,'Auriculares hyperX', 2)
