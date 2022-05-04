
class Produto():
    def __init__(self, codigo, nome, valor) -> None:
        self._codigo: int = codigo
        self._nome: str = nome
        self._valor: float = valor
        self.incluirProduto(self)
    
    produtos = []

    def incluirProduto(self, produto):
        Produto.produtos.append(produto)

    def alterarProduto(self, codigo, nome, valor):

        self._codigo = codigo
        self._nome = nome
        self._valor = valor

    def imprimeListaProduto(self):
        print(Produto.produtos)

    def __str__(self) -> str:
        return f'{self._nome} {self._codigo} {self._valor}'

    def __repr__(self) -> str:
        return f'({self._nome}, {self._codigo}, {self._valor})'
        

if __name__ == '__main__':
    p = Produto(1, 'aaaa', 1200)
    p1 = Produto(2, 'aaaddfsdfa', 100)
    p2 = Produto(3, 'afdfa', 1300)

    print(p)
    print(p1)
    print(p2)

    p.imprimeListaProduto()
    

