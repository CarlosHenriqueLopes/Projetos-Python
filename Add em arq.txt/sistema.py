from interface import *
from format_arquivo import *
from time import sleep

arquivo = 'cadastro.txt'
if not arquivo_existe(arquivo):
    criar_arquivo(arquivo)

while True:
    per = menu_list(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    sleep(0.5)
    if per == 1:
        ler_arquivo(arquivo)
    elif per == 2:
        titulo('NOVO CADASTRO')
        nome = str(input('NOME: '))
        idade = leia_int('IDADE: ')
        cadastrar(arquivo, nome, idade)
    elif per == 3:
        print('saindo do sistema...')
        break
    else:
        print('opção invalida')
    sleep(1)

sleep(1)
titulo('Sistema encerrado')