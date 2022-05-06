from typing import List
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt


from src.Cliente import Cliente
from src.Produto import Produto
from src.Venda import Venda
from src.utils import strToDate
from src.manipulador import alterarEntidade, excluirEntidade, printListaNumerada

console = Console()

def display_menu(options: List ,title: str, prompt: str) -> int:
    """
    params:
        options : List of Text objects, the options to be displayed in the menu
        title : menu's title (str)
        prompt : input prompt (str)
    """
    g_size = 0
    for option in options:
        g_size = len(option) if len(option) > g_size else g_size
    # generating options string
    idx = 1
    menu_str = Text()
    for option in options:
        points = Text('.........') # TAMANHO FIXO + INDICE = 10 espaços
        if g_size > len(option):
            diff = g_size - len(option)
            points += Text('.'*diff)

        menu_str += option + points + Text(str(idx), style='i') + Text('\n')
        idx += 1
        
    menu_str = menu_str[:-1] # removing last \n
    
    # printing the menu
    p = Panel.fit(
            menu_str,
            padding=(1, 3),
            title="[b white]" + title,
            border_style='#c300d9',
            
        )
    console.print(p)

    op = Prompt.ask(prompt, choices=[str(i) for i in range(1, idx)])  # loop here until avaliable option is chosen
    return int(op)


def menuPrincipal():
    opcoes = [
        Text("Cliente"),
        Text("Produto"),
        Text("Venda")
    ]
    while True:
        op = display_menu(opcoes, 'Menu', "Selecione uma entidade para mais opções")
        if op == 1: # cliente
            while True:
                oc = display_menu(
                    [Text("Incluir"), Text('Excluir'), Text("Alterar dados"), Text('Visualizar dados'), Text('Voltar')], 
                    'Opções para cliente', 'Escolha uma opção'
                    )

                if oc == 1:
                    # incluirCliente
                    nome = input('Nome: ')
                    endereco = input('Endereço: ')
                    rg = input('Número do RG: ')
                    datan = input('Data de nascimento (dd/mm/aaaa): ')
                    
                    
                    cliente = Cliente(nome, endereco, rg, datan)
                    console.print('Cliente incluído com sucesso', style='green')
                    print(cliente)

                elif oc == 2: # excluir
                    if Cliente.clientes:
                        excluirEntidade('cliente', Cliente.clientes)
                    else:
                        print('Não há clientes cadastrados')
                elif oc == 3: # alterar 
                    if Cliente.clientes:
                        alterarEntidade('cliente', Cliente.clientes)
                        console.print('Dados alterados com sucesso', style='green')
                    else:
                        print('Não há clientes cadastrados')

                elif oc == 4: # Visualizar
                    if Cliente.clientes:
                        print('Visualizar dados do cliente')
                        printListaNumerada([c.nome for c in Cliente.clientes])
                        p = Prompt.ask('Selecione um cliente ', choices=[str(x) for x in range(1, len(Cliente.clientes)+1)])
                        p = int(p) - 1
                        Cliente.clientes[p].visualizarCliente()
                    else:
                        print('Não há clientes cadastrados')

                elif oc == 5: # voltar
                    break

        elif op == 2: # Produto
            while True:
                opr = display_menu(
                    [Text("Incluir"), Text('Excluir'), Text("Alterar dados"), Text('Visualizar dados'), Text('Voltar')], 
                    'Opções para produto', 'Escolha uma opção'
                    )

                if opr == 1:
                    nomep = input('Nome: ')
                    valor = input('Valor: ')

                    produto = Produto(nomep, float(valor))

                    console.print(f'produto incluído com sucesso', style='green')
                    print(produto)
                
                elif opr == 2: # excluir
                    if Produto.produtos:
                        excluirEntidade('produto', Produto.produtos)
                    else:
                        print('Não há produtos cadastrados')

                elif opr == 3: # alterar
                    if Produto.produtos:
                        alterarEntidade('produto', Produto.produtos)
                    else:
                        print('Não há produtos cadastrados')

                elif opr == 4: # vizualizar
                    if Produto.produtos:
                        print('Vizualizar dados do produto')
                        printListaNumerada([p.nome for p in Produto.produtos])
                        p = Prompt.ask('Selecione um produto ', choices=[str(x) for x in range(1, len(Produto.produtos)+1)])
                        p = int(p) - 1
                        Produto.produtos[p].visualizarProduto()
                    else:
                        print('Não há produtos cadastrados')

                elif opr == 5: # voltar
                    break
                    


        elif op == 3:
            while True:
                opr = display_menu(
                    [Text("Incluir"), Text('Excluir'), Text('Visualizar dados'), Text('Voltar')], 
                    'Opções para venda', 'Escolha uma opção'
                    )
                if opr == 1:
                    venda = Venda()
                    console.print(f'Venda incluída com sucesso', style='green')

                elif opr == 2:
                    if Venda.vendas:
                        excluirEntidade('venda', Venda.vendas)
                    else:
                        print('Não há vendas cadastradas')

                elif opr == 3:
                    if Venda.vendas:
                        print('Vizualizar dados da venda')
                        i = 1
                        for n, d in zip([v.numero for v in Venda.vendas], [v.data for v in Venda.vendas]):
                            print(f'{i}. Venda Nº: {n} Data: {d}')
                            i += 1
                        p = Prompt.ask('Selecione uma venda ', choices=[str(x) for x in range(1, len(Venda.vendas)+1)])
                        p = int(p) - 1
                        Venda.vendas[p].visualizarVenda()
                    else:
                        print('Não há vendas cadastradas')

                elif opr == 4: # voltar
                    break



if __name__ == '__main__':
    menuPrincipal()
# NOTE
# menu em linha de comando que permite a inclusão, alteração, remoção e visualização dos dados das entidades abaixo
# menu principal:
    # clientes
    # produtos
    # vendas

    # submenu
        # incluir
        # alterar 
        # excluir
        # vizualizar