from ClienteDAO import ClienteDAO
from Cliente import Cliente

#clientes = [Cliente(12, "joao"), Cliente(4, "maria")]
cliente_dao = ClienteDAO()

cliente = cliente_dao.get(4)
print(cliente.nome, ':', cliente.codigo)

cliente = cliente_dao.get(12)
print(cliente.nome, ':', cliente.codigo)

#for cliente in clientes:
#    cliente_dao.add(cliente)
