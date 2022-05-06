from src.Totalizavel import Totalizavel
from src.Produto import Produto

from rich.prompt import Prompt, IntPrompt

class ItemVenda(Totalizavel):
    def __init__(self) -> None:
        super().__init__()
        self._produto: Produto = self._addProduto()
        self._valor: float = self._produto.valor
        self._qtd: int = int(input('Informe a quantidade: '))

    @property
    def produto(self):
        return self._produto

    @property
    def valor(self):
        return self._valor

    def total(self) -> float:
        return self._valor * self._qtd
    
    def _addProduto(self):
        produtos = Produto.produtos
        i = 1
        for prod in produtos:
            print(f'{i}. {prod.nome} → R$ {prod.valor}')
            i += 1
        p = Prompt.ask('Escolha um produto', choices=[str(x) for x in range(1, len(produtos)+1)])

        p = int(p) - 1
        return Produto.produtos[p]
                
    def __repr__(self) -> str:
        return f"\nProduto: {self._produto.nome}\nValor: R$ {self._valor}\nQtd: {self._qtd}\nTotal: R$ {self.total():,.2f}"





