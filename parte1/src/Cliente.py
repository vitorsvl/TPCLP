from sqlite3 import Date
from tokenize import String
from Pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, rg, dataNasc) -> None:
        super().__init__()
        self._rg: String = rg
        self._dataNasc: Date = dataNasc