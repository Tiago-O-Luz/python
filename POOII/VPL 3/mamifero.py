from abc import ABC, abstractmethod
from animal import Animal

class Mamifero(Animal, ABC): 
    @abstractmethod
    def __init__(self, volumeSom: int, tamanhoPasso: int):
        super().__init__(tamanhoPasso)
        self.volume_som = volumeSom

    @property
    def volume_som(self):
        return self.__volume_som

    @volume_som.setter
    def volume_som(self, volumeSom):
        self.__volume_som = volumeSom
    
    def produzirSom(self):
        return "MAMIFERO: PRODUZ SOM: "