from colorama import *
init(autoreset=True)

def leia_int(li):
    while True:
        try:
            n = int(input(li))
        except (ValueError, TypeError):
            print('ERRO - Digito invalido')
        except KeyboardInterrupt:
            print('ERRO - Usuário preferiu parar')
        else:
            return n


def linha(l=30):
    return Style.BRIGHT + '=' * l


def titulo(t):
    print(linha())
    print(Fore.MAGENTA + t.center(30))
    print(linha())


def menu_list(menu_list):
    titulo('MENU PRINCIPAL')
    cont = 1
    for c in menu_list:
        print(Fore.GREEN + f'{cont} - {c}')
        cont += 1
        print()
    print(linha())
    return leia_int(Fore.CYAN + 'Escolha uma opção: ')