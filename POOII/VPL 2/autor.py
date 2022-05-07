

class Autor:
    def __init__(self, codigo: int, nome: str):
        self.__codigo = codigo
        self.__nome = nome

    @property
    def codigo(self):
        return self.__codigo

    @property
    def nome(self):
        return self.__nome

    @codigo.setter
    def codigo(self, cod):
        self.__codigo = cod

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
