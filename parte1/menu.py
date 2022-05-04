from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt


def display_menu(options):
    """
    param options : List of Text objects, the options to be displayed in the menu
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
            title="[b white]Menu",
            border_style='#c300d9',
            
        )
    Console().print(p)

    op = Prompt.ask("escolha uma opção", choices=[str(i) for i in range(1, idx)])  # loop here until avaliable option is chosen
    return int(op)


if __name__ == '__main__':
    options = [
        'opção 1',
        'opção 2',
        'opção 3',
        'opção 4'
    ]
    options = list(map(Text, options))
    Console().print(options)
    display_menu(options)