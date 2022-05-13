from abc import ABC, abstractmethod
from animal import Animal

class Ave(Animal):
    @abstractmethod
    def __init__(self, tamanhoPasso: int, alturaVoo: int):
        super().__init__(tamanhoPasso)
        self.__altura_voo = alturaVoo
    
    @property
    def altura_voo(self):
        return self.__altura_voo

    @altura_voo.setter
    def altura_voo(self, alturaVoo):
        self.__altura_voo = alturaVoo
    
    def mover(self):
        return "ANIMAL: DESLOCOU "+str(self.tamanho_passo)+" VOANDO"

    def produzirSom(self):
        return  "AVE: PRODUZ SOM: "