from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, tamanhoPasso: int):
        self.__tamanho_passo = tamanhoPasso

    @property
    def tamanho_passo(self):
        return self.__tamanho_passo
        
    @tamanho_passo.setter
    def tamanho_passo(self, tamanhoPasso):
        self.__tamanho_passo = tamanhoPasso

    def mover(self):
        return "ANIMAL: DESLOCOU "+str(self.tamanho_passo)
        
    @abstractmethod
    def produzirSom(self):
        pass