from datetime import date
from src.Pessoa import Pessoa

class Cliente(Pessoa):
    clientes = [] # lista de clientes
    def __init__(self, nome, endereco, rg, dataNasc) -> None:
        super().__init__(nome, endereco)
        self._rg: str = rg
        self._dataNasc: date = dataNasc
        print(type(self._dataNasc))
        self._incluirCliente(self) # inclui o cliente na lista no momento da inicialização

    def _incluirCliente(self, cliente):
        Cliente.clientes.append(cliente)

    def alterarCliente(self, nome, endereco, rg, dataNasc):
        if nome:
            self._nome = nome
        if endereco:
            self._endereco = endereco
        if rg:
            self._rg = rg
        if dataNasc:
            self._dataNasc = dataNasc
        index = Cliente.clientes.index(self)
        Cliente.clientes[index] = self 
        
    def excluir(self):
        index = Cliente.clientes.index(self)
        Cliente.clientes.pop(index)
        
    def imprimeListaCliente(self): 
        i = 1
        for p in Cliente.clientes:
            print(f'{i}. {p}')

    def visualizarCliente(self):
        print('-------------------------')
        print(self)
        print('-------------------------')

    def __str__(self) -> str:
        return f'\nNome: {self._nome}\nEndereço: {self._endereco}\nrg: {self._rg}\ndata de nascimento: {self._dataNasc.strftime("%d/%m/%Y")}'

    def __repr__(self) -> str:
        return f'({self._nome}, {self._endereco}, {self._rg}, {self._dataNasc})'
        
