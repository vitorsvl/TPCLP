
class Pessoa():
    def __init__(self, nome, endereco) -> None:
        self._nome: str = nome # aqui ficam os atributos
        self._endereco: str = endereco

    @property
    def nome(self):
        return self._nome