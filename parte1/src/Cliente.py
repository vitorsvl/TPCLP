from datetime import date
from Pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome, endereco, rg, dataNasc) -> None:
        super().__init__(nome, endereco)
        self._rg: str = rg
        self._dataNasc: date = dataNasc

