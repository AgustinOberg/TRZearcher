from pages_reader import PagesReader
class Interface:

    def __init__(self):
        self.pages = ["Compra Gamer", "Gezatek", "Venex", "Full H4rd"]
        self.active_pages = []
        self.pages_to_search = PagesReader().get_url()
        self.search_type = 1
        self.__message_product_to_search()
        self.__message_pages_to_search()
        self.__message_search_type()
        self.__results()



    def __message_product_to_search(self):
        self.product = input("***************************************************************"
                                     + "\n"
                                     + "\n                     CHOOGLE"
                                     + "\n                       TRZ"
                                     + "\n"
                                     + "\n Somos un buscador/comparador de precios de productos GAMERS"
                                     + "\n"
                                     + "\n Introduzca el producto a buscar: ")

    def __message_pages_to_search(self):
        print("\n***************************************************************"
              + "\n"
              + "\n Responder con un si en el caso de querer incluirla")
        i = 0
        for page in self.pages:
            boolean = input(
                "\n Quieres incluir en tu comparacion a " + str(page) + "? ")
            if (boolean.lower() == "si"):
                self.active_pages.append(self.pages_to_search[i])
                i+=1

    def __message_search_type(self):
        self.search_type = input("\n ¿ Que tipo de busqueda quieres realizar ?"
                                 + "\n"
                                 + "\n 1 - Publicación con la frase exacta"
                                 + "\n 2 - Publicación que contenga todas las palabras"
                                 + "\n 3 - Publicación que contenga algunas de las palabras"
                                 + "\n"
                                 + "\n ")

    def __results(self):
        print("\n***************************************************************"
              + "\n"
              + "\n Se realizara la una busqueda de " +
              str(self.pages_to_search)
              + "\n "
              + "\n Tipo: " + str(self.search_type)
              + "\n "
              + "\n En las siguientes paginas:")
        for page in self.active_pages:
            print("- " + str(page))

    def get_pages_to_search(self):
        return self.active_pages

    def get_product_to_search(self):
        return self.pages_to_search

    def get_search_type(self):
        return self.search_type
