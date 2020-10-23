# A través del método get_url, brinda las url configuradas

class PagesReader:
    def __init__(self):
        self.file_name = 'pages.txt'
        self.__read_url__()

    def __read_url__(self):
        with open(self.file_name, 'r') as pages_file:
            self.pages = list(map(str.rstrip, pages_file))

    def get_url(self):
        return self.pages
