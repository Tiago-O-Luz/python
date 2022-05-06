

class Produto:

    def __init__(self, codigo, descricao, categoria):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__categoria = categoria
        
        self.__quantidade = 0
        self.__preco_unitario = 0
        self.__cliente = None

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, cod):
        self.__codigo = cod

    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, desc):
        self.__descricao = desc

    @property
    def categoria(self):
        return self.__categoria
    
    @categoria.setter
    def categoria(self, cat):
        self.__categoria = cat

    @property
    def quantidade(self):
        return self.__quantidade
    
    @quantidade.setter
    def quantidade(self, qtd):
        self.__quantidade = qtd

    @property
    def preco_unitario(self):
        return self.__preco_unitario
    
    @preco_unitario.setter
    def preco_unitario(self, prc):
        self.__preco_unitario = prc

    @property
    def cliente(self):
        return self.__cliente
    
    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente
    
    def preco_total(self):
        return self.__quantidade * self.__preco_unitario
