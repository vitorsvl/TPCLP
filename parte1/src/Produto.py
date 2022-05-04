
class Produto():
    
    produtos = [] # lista de produtos

    def __init__(self, codigo, nome, valor) -> None:
        self._codigo: int = codigo
        self._nome: str = nome
        self._valor: float = valor
        self.incluirProduto(self)

    def incluirProduto(self, produto):
        Produto.produtos.append(produto)

    def alterarProduto(self, nome, valor):
        self._nome = nome
        self._valor = valor
        index = Produto.produtos.index(self)
        Produto.produtos[index] = self # ??
        

    def excluirProduto(self):
        index = Produto.produtos.index(self)
        produtos.pop(index)
        

    def imprimeListaProduto(self):
        print(Produto.produtos)

    def vizualizarProduto(self):
        print(f'nome: {self._nome}\ncódigo: {self._codigo}\nvalor: ${self._valor:.2f}')

    def __str__(self) -> str:
        return f'{self._nome} {self._codigo} {self._valor}'

    def __repr__(self) -> str:
        return f'({self._nome}, {self._codigo}, {self._valor})'
        

if __name__ == '__main__':
    p = Produto(1, 'arroz', 23.99)
    p1 = Produto(2, 'chocolate', 10.00)
    p2 = Produto(3, 'banana', 1.49)

    p.imprimeListaProduto()

    p.alterarProduto('leite', 4.29)
    p2.alterarProduto('farinha', 2.99)

    p.imprimeListaProduto()
    print()
    for pp in p.produtos:
        pp.vizualizarProduto()
        print()
    

