from mamifero import Mamifero

class Gato(Mamifero):
    def __init__(self):
        volumeSom, tamanhoPasso = 2, 2
        super().__init__(volumeSom, tamanhoPasso)
    
    def miar(self):
        return self.produzirSom()+str(self.volume_som)+" SOM: MIAU"