from tokenize import String


class Produto():
    def __init__(self, codigo, nome, valor) -> None:
        self._codigo: int = codigo
        self._nome: String = nome
        self._valor: float = valor