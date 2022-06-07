

class Pessoa:
    def __init__(self, nome: str) -> None:
        self.__nome = nome
    
    @property
    def nome(self):
        return self.__nome