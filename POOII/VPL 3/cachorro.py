from mamifero import Mamifero

class Cachorro(Mamifero):
    def __init__(self):
        volumeSom, tamanhoPasso = 3, 3
        super().__init__(volumeSom, tamanhoPasso)

    def latir(self):
        return self.produzirSom()+str(self.volume_som)+" SOM: AU"