import random

def titulo(t):
    tam_linha = len(t) + 2
    print('=' * tam_linha)
    print(t.center(tam_linha))
    print('=' * tam_linha)


# jogo de cara ou coroa

moeda = ['CARA', 'COROA']
moeda = random.choice(moeda)
print(moeda)
titulo('Desafio cara ou coroa')

n = str(input('Escolha entra CARA ou COROA: ')).upper().strip()
if n == moeda:
    print(f'MOEDA: {moeda}')
    print('Parabéns acertou!')
else:
    print(f'MOEDA: {moeda}')
    print('Que pena, tente outra')


#-------------------------------------------------------------------------------------------

nomes = ['nome1', 'nome2', 'nome3']

titulo('Escolha uma nome dentro da lista, e tente acertar a escolha da maquina:')
lista_pergunta = str(input(f'{nomes}: '))

random.shuffle(nomes) # -> embaralhando a lista
nome_maquina = random.choice(nomes) # -> escolhendo um valor da lista sorteada

print(nomes)
print(nome_maquina)
if lista_pergunta == nome_maquina:
    print(f'Nome escolhido: {nome_maquina}')
    print('Parabéns! Você acertou')
else:
    print(f'Nome escolhido: {nome_maquina}')
    print('Que pena, tente novamento')