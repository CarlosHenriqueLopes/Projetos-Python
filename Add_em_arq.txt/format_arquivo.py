from interface import *

def arquivo_existe(nome_arquivo):
    try:
        a = open(nome_arquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(x):
    try:
        a = open(x, 'wt+')
        a.close()
    except:
        print(Fore.RED + 'Houve um erro na criação do arquivo')
    else:
        print(Fore.LIGHTCYAN_EX + f'Arquivo {x} criado com sucesso!')


def ler_arquivo(la):
    try:
        a = open(la, 'rt')
    except:
        print(Fore.RED + 'Houve um erro. Não foi possível abrir o arquivo')
    else:
        titulo('PESSOAS CADASTRADAS')
        for c in a:#OBS: formatação do print
            dados = c.split('-')
            dados[1] = dados[1].replace('\n', '')
            print(f'{dados[0]:<20}{dados[1]:>2} anos')
    finally:
        a.close()


def cadastrar(arquivo, nome='Desconhecido', idade=0):
    try:
        a = open(arquivo, 'at')
    except:
        print(Fore.RED + 'Houve um erro na abertura do arquivo')
    else:
        try:#OBS: formatação do print simplificada pode ser feita aqui
            a.write(f'{nome}-{idade}\n')
        except:
            print('Houve um erro para escrever o arquivo na def cadastrar')
        else:
            print(f'Novo registro de {nome} foi adicionado com ao cadastro')
            a.close()