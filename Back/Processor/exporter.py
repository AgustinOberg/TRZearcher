import csv
from datetime import datetime
import json


class Exporter:

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
            str(self.date.month) + "-" + str(self.date.year)

    def write_csv(self):
        """
        El archivo .csv generado tendrá por nombre la búsqueda y la fecha en que se realizó.
        Escribe los productos que fueron pasados por parámetro en el constructor en él.
        """
        file = open(self.file_name + ".csv", "w", newline='\n', encoding="utf-8")
        with file:
            write = csv.writer(file)
            write.writerow(["Page", "Category", "Title", "Price", "Link", "Time"])
            for product in self.ordered_products:
                write.writerow(product)

    def write_html(self):
        """
        El archivo .html generado tendrá por nombre la búsqueda y la fecha en que se realizó.
        Escribe los productos que fueron pasados por parámetro en el constructor en él.
        """

        base = '''
        <!DOCTYPE html>
        <html lang="en">

        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>TRZ</title>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css"
                integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
        </head>

        <body class="container">
            <h1 class="text-center mt-4">TRZearcher</h1>
            <hr>
            <h5 class="text-center font-weight-bold">Busqueda</h5>
            <table class="table table-striped">
                <thead>
                    <tr>
                        <th scope="col">Category</th>
                        <th scope="col">Title</th>
                        <th scope="col">Price</th>
                        <th scope="col">Time</th>
                    </tr>
        </thead>
        <tbody>

        '''
        file = open(self.file_name + ".html", "w", newline='\n', encoding="utf-8")
        with file:
            file.write(base)
            for product in self.ordered_products:
                string_product = '<tr> <th scope="row">' + product[1] + '</th> <td> <a href="' + product[4] + '" target="_blank">' + \
                                 product[2] + '</a> </td> <td>' + str(product[3]) + '</td> <td>' + product[5] + '</td> </tr>'

                file.write(string_product.replace('\x93', " ").strip())

            final_string = '''
                     </tbody>
                   </table>
                </body>
            </html>
            '''
            file.write(final_string)
            file.close()

    def write_json(self):
        file = open(self.file_name + ".json", "w", newline='\n')
        final_dict = dict()
        final_dict["products"] = list()
        for product in self.ordered_products:
            dict_json = self.__make_product_dict(product)
            final_dict["products"].append(dict_json)
        with file:
            json.dump(final_dict, file, indent=2)


    def __make_product_dict(self, list):
        keys = ["Page", "Category", "Title", "Price", "Link", "Time"]
        dictionary = dict()
        i = 0
        for key in keys:
            dictionary[key] = list[i]
            i+=1
        return dictionary