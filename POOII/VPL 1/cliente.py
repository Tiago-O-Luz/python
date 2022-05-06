

class Cliente:

    def __init__(self, nome, telefone):
        self.__nome = nome
        self.__fone = telefone
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nm):
        self.__nome = nm

    @property
    def fone(self):
        return self.__fone
    
    @fone.setter
    def fone(self, tl):
        self.__fone = tl
