from abstractElevador import AbstractElevador
from elevadorCheioException import ElevadorCheioException
from elevadorJahNoTerreoException import ElevadorJahNoTerreoException
from elevadorJahNoUltimoAndarException import ElevadorJahNoUltimoAndarException
from elevadorJahVazioException import ElevadorJahVazioException


class Elevador(AbstractElevador):
    def __init__(self, andarAtual: int, totalAndaresPredio: int, capacidade: int, totalPessoas: int):
        super().__init__()
        self.__capacidade = capacidade
        self.__andarAtual = andarAtual
        self.__totalPessoas = totalPessoas
        self.__totalAndaresPredio = totalAndaresPredio
    
    @property
    def capacidade(self) -> int:
        return self.__capacidade

    @property
    def totalPessoas(self) -> int:
        return self.__totalPessoas

    @property
    def totalAndaresPredio(self) -> int:
        return self.__totalAndaresPredio

    @property
    def andarAtual(self) -> int:
        return self.__andarAtual

    @totalAndaresPredio.setter
    def totalAndaresPredio(self, totalAndaresPredio: int):
        self.__totalAndaresPredio = totalAndaresPredio

    def subir(self) -> str:
        if self.andarAtual == self.totalAndaresPredio:
            raise ElevadorJahNoUltimoAndarException('')
        else:
            self.andarAtual += 1
            return str(self.andarAtual)

    def descer(self) -> str:
        if self.andarAtual == 0:
            raise ElevadorJahNoTerreoException('')
        else:
            self.andarAtual -= 1
            return str(self.andarAtual)
    
    def entraPessoa(self) -> str:
        if self.totalPessoas == self.capacidade:
            raise ElevadorCheioException('Capacid')
        else:
            self.totalPessoas += 1
            return str(self.totalPessoas)

    def saiPessoa(self) -> str:
        if self.totalPessoas == 0:
            raise ElevadorJahVazioException
        else:
            self.totalPessoas -=1
            return str(self.totalPessoas)