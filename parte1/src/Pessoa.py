
from tokenize import String


class Pessoa():
    def __init__(self, nome, endereco) -> None:
        self._nome: String = nome # aqui ficam os atributos
        self._endereco: String = endereco


    # aqui os métodos
    # def metodo(parametros):
        # código