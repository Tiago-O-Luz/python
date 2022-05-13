from ave import Ave

class Canarinho(Ave):
    def __init__(self, tamanhoPasso: int, alturaVoo: int):
        super().__init__(tamanhoPasso, alturaVoo)

    def cantar(self):
        return self.produzirSom()+"PIU"