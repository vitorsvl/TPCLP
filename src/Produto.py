
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

    @property
    def valor(self):
        return self._valor

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
        
    def visualizarProduto(self):
        print('-------------------------')
        print(self)
        print('-------------------------')


    def __str__(self) -> str:
        return f'Nome: {self._nome}\nValor: {self._valor}\nCódigo: {self._codigo}'

    def __repr__(self) -> str:
        return f'({self._nome}, {self._codigo}, {self._valor})'
        
