
from datetime import date
from typing import List

from src.Cliente import Cliente
from src.Totalizavel import Totalizavel
from src.ItemVenda import ItemVenda

from rich.prompt import Prompt, Confirm


class Venda(Totalizavel):
    cont = 0

    def __init__(self) -> None:
        super().__init__()
        self._numero: int = Venda.cont
        Venda.cont += 1
        self._data: date = date.today()
        self._cliente: Cliente = self.selecionarCliente()
        self._itens: List = self.addItens()
        self._realizarVenda(self)

    vendas = []

    @property
    def numero(self):
        return self._numero

    @property
    def data(self):
        return self._data.strftime("%d/%m/%Y")

    def addItens(self):
        print('Adicionar itens')
        item = ItemVenda()
        itens = []
        itens.append(item)
        print('Produto adicionado!')
        while True:
            if Confirm.ask('Adicionar outro item à venda?'):
                item = ItemVenda()
                itens.append(item)
                print('Produto adicionado!')
            else:
                break
        return itens 


    def selecionarCliente(self):
        clientes = Cliente.clientes
        i = 1
        for c in clientes:
            print(f'{i}. {c.nome} RG: {c.rg}' )
            i += 1
        p = Prompt.ask('Escolha um cliente', choices=[
                       str(x) for x in range(1, len(clientes)+1)])
        p = int(p) - 1
        return Cliente.clientes[p]

    def _realizarVenda(self, venda):
        Venda.vendas.append(venda)

    def excluir(self):
        index = Venda.vendas.index(self)
        Venda.vendas.pop(index)

    def visualizarVenda(self):
        d =  self._data.strftime("%d/%m/%Y")
        s1 = f'{"VENDA".center(42)} \n→ Nº: {self._numero}  Data: {d}  Cliente: {self._cliente.nome}\n\n'
    
        s2 = 'ITENS:\n'
        for item in self._itens:
            s2 = s2 + str(item) + '\n'
        s3 = f'\nTotal da Venda: R$ {self.total():,.2f}'
        print('-'*42)
        print(s1 + s2 + s3)
        print('-'*42)

    def __str__(self) -> str:
        d =  self._data.strftime("%d/%m/%Y")
        return f"VENDA → Nº: {self._numero}\nData: {d}\nCliente: {self._cliente.nome}\nItens: {self._itens}\nTotal da Venda: R$ {self.total()}"

    # return f'({self._nome}, {self._codigo}, {self._valor})'

    def total(self) -> float:
        return sum([item.total() for item in self._itens])


if __name__ == '__main__':
    from Produto import Produto
    c1 = Cliente('Paula', 'n sei', 'nsei', '04/12/2000')
    p1 = Produto('arroz', 23.99)
    p2 = Produto('milho', 3.99)
    p3 = Produto('gengibre', 1.99)

    print(Produto.produtos)
    
    v = Venda()
    
    v.visualizarVenda()