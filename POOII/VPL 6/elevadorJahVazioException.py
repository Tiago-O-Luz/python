class ElevadorJahVazioException(Exception):
    def __init__(self):
        super().__init__("O elevador esta está vazio!")
