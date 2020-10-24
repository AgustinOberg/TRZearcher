class Interface:

    def __init__(self):
        self.pages = ["Compra Gamer", "Gezatek", "Venex", "Full H4rd"]
        self.pages_to_search = []
        self.product_to_search = ""
        self.__message_product_to_search()
        self.__message_pages_to_search()
        self.__results()
        print("\n Los resultados seran exportados en un CSV con el nombre de " +
              str(self.product_to_search) + ".csv")

    def __message_product_to_search(self):
        self.product_to_search = input("***************************************************************"
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
        for page in self.pages:
            boolean = input(
                "\n Quieres incluir en tu comparacion a " + str(page) + "? ")
            if (boolean.lower() == "si"):
                self.pages_to_search.append(page)

    def __results(self):
        print("\n***************************************************************"
              + "\n"
              + "\n Se realizara la una busqueda de " +
              str(self.product_to_search)
              + "\n "
              + "\n En las siguientes paginas:")
        for page in self.pages_to_search:
            print("- " + str(page))
