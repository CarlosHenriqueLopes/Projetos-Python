from random import randint
numero = randint(1, 100)


def titulo(t):
    print('=' * 30)
    print(f'{t}'.center(30))
    print('=' * 30)


def subtt(x):
    print('-' * len(x))
    print(x.center(len(x)))
    print('-' * len(x))

    

cont = tentativas = 1
titulo(' ADIVINHE O NUMERO') #def titulo

subtt(' Escolha um numero entre 1 a 100') #def subtt

while True:
    print(numero)
    pergunta = int(input(' ESCOLHA UM NUMERO: '))
    if cont == 3:
        if pergunta != numero:
            if numero % 2 == 1:
                print(' Uma dica! É um numero IMPAR')
            elif numero % 2 == 0:
                print(' Uma dica! É um numero PAR')
    if pergunta < numero:
        print(' vc esta proximo')
        cont += 1
        tentativas += 1
    if pergunta > numero:
        print(' vc passou')
        cont += 1
        tentativas += 1
    if pergunta == numero:
        print(f' Acertou!, O numero escolhido foi {numero}')
        break
subtt(f' Você acertou em {tentativas} tentativas')
titulo(' FIM, OBRIGADO POR JOGAR')
