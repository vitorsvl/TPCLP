from rich.prompt import Prompt, Confirm


def printListaNumerada(lista):
    i = 1
    for p in lista:
        print(f'{i}. {p}')
        i += 1


def excluirEntidade(nome, lista):
    """
    Exclui uma entidade.
    Parâmetros:
        nome: nome(tipo) da entidade [cliente, produto, venda, item]
        lista: lista de objetos da entidade escolhida
    """

    if nome == 'venda':
        i = 1
        for n, d in zip([v.numero for v in lista], [v.data for v in lista]):
            print(f'{i}. Venda Nº: {n} |  Data: {d}')
        p = Prompt.ask('Selecione uma venda ', choices=[str(x) for x in range(1, len(lista)+1)])
        p = int(p) - 1
        if Confirm.ask(f'Excluir {nome} Nº{lista[p].numero} ?'):
            lista[p].excluir()
            print(f'{nome} excluída com sucesso')
    else:
        print(f'Qual {nome} deseja excluir? ')
        printListaNumerada([e.nome for e in lista])
        p = Prompt.ask('Escolha uma opção ', choices=[str(x) for x in range(1, len(lista)+1)])
        p = int(p) - 1
        if Confirm.ask(f'Excluir {nome} {lista[p].nome} ?'):
            lista[p].excluir()
            print(f'{nome} excluído com sucesso')


def alterarEntidade(nome, lista):
    """
    Altera os dados de uma entidade.
    Parâmetros:
        nome: nome(tipo) da entidade [cliente, produto, venda, item]
        lista: lista de objetos da entidade escolhida
    """
    if nome == 'produto':
        print(f'Deseja alterar os dados de qual {nome} ?')
        printListaNumerada([e.nome for e in lista])
        p = Prompt.ask('Escolha uma opção ', choices=[str(x) for x in range(1, len(lista)+1)])
        p = int(p) - 1

        n = input('Digite o novo nome ou ENTER para não alterar: ')
        v = input('informe o novo valor ou ENTER para não alterar: ')

        lista[p].alterarProduto(n, v)
        print(f'{nome} alterado:', lista[p])

    elif nome == 'cliente':
        print(f'Deseja alterar os dados de qual {nome} ?')
        printListaNumerada(lista)
        p = Prompt.ask('Escolha uma opção ', choices=[str(x) for x in range(1, len(lista)+1)])
        p = int(p) - 1

        n = input('Digite o novo nome ou ENTER para não alterar: ')
        e = input('Digite o novo endereço ou ENTER para não alterar: ')
        rg = input('Digite o novo RG ou ENTER para não alterar: ')
        d = input('Digite a nova data de nascimento ou ENTER para não alterar (DD/MM/AAAA): ')

        lista[p].alterarCliente(n, e, rg, d)

    else:
        print(f'Entidade {nome} não encontrada')


