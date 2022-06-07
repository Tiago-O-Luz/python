from Pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, codigo: int, nome: str) -> None:
        super().__init__(nome)
        self.__codigo = codigo
    
    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo