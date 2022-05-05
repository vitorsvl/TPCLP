
from datetime import date
from typing import List

from Cliente import Cliente
from Totalizavel import Totalizavel

class Venda(Totalizavel):
    def __init__(self, numero, data, cliente, itens) -> None:
        super().__init__()
        self._numero: int = numero
        self._data: date = data
        self._cliente: Cliente = cliente # falta implementar Cliente
        self._itens: List = itens 
    

    def total(self) -> float:
        return sum([item.total() for item in self._itens])