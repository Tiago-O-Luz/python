from abstractControladorElevador import AbstractControladorElevador
from comandoInvalidoException import ComandoInvalidoException
from elevador import Elevador


class ControladorElevador(AbstractControladorElevador):
    def __init__(self, andarAtual: int, totalAndaresPredio: int, capacidade: int, totalPessoas: int):
        self.inicializarElevador(andarAtual, totalAndaresPredio, capacidade, totalPessoas)

    '''
    Faz o elevador subir um andar. Se jah estiver no ultimo andar, dispara excecao
    @return Mensagem informando o que ocorreu com o elevador 
    @throws ElevadorJahNoUltimoAndarException 
    '''
    def subir(self) -> str:
        pass

    '''
    Faz o elevador descer um andar. Se jah estiver no terreo, dispara excecao
    @return Mensagem informando o que ocorreu com o elevador
    @throws ElevadorJahNoTerreoException
    '''
    def descer(self) -> str:
        pass

    '''
    Entra uma pessoa no Elevador. Se nao for possivel permitir a entrada da pessoa, dispara excecao
    @return Mensagem informando o que ocorreu com o elevador
    @throws ElevadorCheioException
    '''
    def entraPessoa(self) -> str:
        pass

    '''
    Sai uma pessoa no Elevador. Se nao for possivel permitir a saida de uma pessoa, dispara excecao
    @return Mensagem informando o que ocorreu com o elevador
    @throws ElevadorJahVazioException
    '''
    def saiPessoa() -> str:
        pass

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
        self.__elevador = Elevador(andarAtual, totalAndaresPredio, capacidade, totalPessoas)
