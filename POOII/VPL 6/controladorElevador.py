from abstractControladorElevador import AbstractControladorElevador
from comandoInvalidoException import ComandoInvalidoException
from elevador import Elevador


class ControladorElevador(AbstractControladorElevador):
    def __init__(self, andarAtual: int = 0, totalAndaresPredio: int = 10, capacidade: int = 10, totalPessoas: int = 5):
        self.inicializarElevador(andarAtual, totalAndaresPredio, capacidade, totalPessoas)

    '''
    Faz o elevador subir um andar. Se jah estiver no ultimo andar, dispara excecao
    @return Mensagem informando o que ocorreu com o elevador 
    @throws ElevadorJahNoUltimoAndarException 
    '''
    def subir(self) -> str:
        return self.elevador.subir()

    '''
    Faz o elevador descer um andar. Se jah estiver no terreo, dispara excecao
    @return Mensagem informando o que ocorreu com o elevador
    @throws ElevadorJahNoTerreoException
    '''
    def descer(self) -> str:
        return self.elevador.descer()

    '''
    Entra uma pessoa no Elevador. Se nao for possivel permitir a entrada da pessoa, dispara excecao
    @return Mensagem informando o que ocorreu com o elevador
    @throws ElevadorCheioException
    '''
    def entraPessoa(self) -> str:
        return self.elevador.entraPessoa()

    '''
    Sai uma pessoa no Elevador. Se nao for possivel permitir a saida de uma pessoa, dispara excecao
    @return Mensagem informando o que ocorreu com o elevador
    @throws ElevadorJahVazioException
    '''
    def saiPessoa(self) -> str:
        return self.elevador.saiPessoa()

    '''
    @return Elevador
    '''
    @property
    def elevador(self) -> Elevador:
        return self.__elevador

    '''
    @param andarAtual andar atual do elevador
    @param totalAndaresPredio total de andares do predio
    @param capacidade capacidade maxima do elevador
    @param totalPessoas total de pessoas atual do elevador
    '''
    def inicializarElevador(self, andarAtual: int, totalAndaresPredio: int, capacidade: int, totalPessoas: int):
        try:
            andarAtual = int(andarAtual)
            totalAndaresPredio = int(totalAndaresPredio)
            capacidade = int(capacidade)
            totalPessoas = int(totalPessoas)
            if (totalAndaresPredio >= 0) and (capacidade >= 0) and (andarAtual >= 0) and (totalPessoas >= 0) and (andarAtual+1 <= totalAndaresPredio) and (totalPessoas <= capacidade):
                self.__elevador = Elevador(andarAtual, totalAndaresPredio, capacidade, totalPessoas)
            else:
                raise ComandoInvalidoException()
        except ValueError:
            raise ComandoInvalidoException()

