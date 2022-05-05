
class Produto():
    
    produtos = [] # lista de produtos
    cont = 0

    def __init__(self, nome, valor) -> None:
        self._codigo: int = Produto.cont
        Produto.cont += 1
        self._nome: str = nome
        self._valor: float = valor
        self._incluirProduto(self) # incluí produto na lista ao instancia-lo

    @property
    def nome(self):
        return self._nome

    def _incluirProduto(self, produto):
        Produto.produtos.append(produto)

    def alterarProduto(self, nome, valor):
        if nome:
            self._nome = nome
        if valor:
            self._valor = valor
        index = Produto.produtos.index(self)
        Produto.produtos[index] = self # ??
        
    def excluir(self):
        index = Produto.produtos.index(self)
        Produto.produtos.pop(index)
        
    def imprimeListaProduto(self): 
        i = 1
        for p in Produto.produtos:
            print(f'{i}. {p}')

    def visualizarProduto(self):
        print('-------------------------')
        print(self)
        print('-------------------------')


    def __str__(self) -> str:
        return f'Nome: {self._nome}\nValor: {self._valor}\nCódigo: {self._codigo}'

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
    

