from Totalizavel import Totalizavel
from Produto import Produto

class ItemVenda(Totalizavel):
    def __init__(self, produto, valor, qtd) -> None:
        super().__init__()
        self._produto: Produto = produto # falta implementar produto
        self._valor: float = valor
        self._qtd: int = qtd

    
    def total(self) -> float:
        return self._valor * self._qtd
