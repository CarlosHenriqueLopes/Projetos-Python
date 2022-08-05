# Alterando cores com a lib colorama
# OBS: usar init(autoreset=True) para cancelar a cor anterior

from random import randint
from time import sleep
from colorama import *
init(autoreset=True)

numero = randint(0, 100)
cont = 1

print(numero) #Lembrete: Para testes (remover esse comando no final)

print(Fore.LIGHTGREEN_EX + Style.BRIGHT + 'Adivinhe um o número escolhido pela maquina, entre 0 e 100')
print(Fore.LIGHTGREEN_EX + Style.BRIGHT + 'Depois de 5 tentativas aparecerá uma dica, logo em seguida aparecerá a opção de mostrar mais uma')
print(Fore.LIGHTGREEN_EX + Style.BRIGHT + 'E logo após 15 tentativas, outra dica aparecerá')
sleep(1.5)

per = ' '
while numero != per:
    per = int(input(Fore.YELLOW + 'Digite um número inteiro de 0 a 100: '))
    if cont == 5:
        if numero % 2 == 0:
            sleep(0.5)
            print(Fore.BLUE + Style.BRIGHT + 'DICA! É um número PAR')
        else:
            sleep(0.5)
            print(Fore.BLUE + Style.BRIGHT + 'DICA! É um número IMPAR')
        sleep(1)
        print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + 'Você está indo bem!')
        sleep(0.5)
        dica = str(input(Fore.BLUE + 'Gostaria de mais dicas? ')).upper().strip()[0]
        sleep(0.5)
        if dica == 'S':
            if numero <= 30:
                print(Fore.BLUE + Style.BRIGHT + 'Está ente 0 a 30')
            elif 30 > numero <= 60:
                print(Fore.BLUE + Style.BRIGHT + 'Está ente 30 a 60')
            else:
                60 > numero <= 100
                print(Fore.BLUE + Style.BRIGHT + 'Está ente 60 a 100')

    elif cont == 15:
        if numero <= 30 and numero % 2 == 0:
            print(Fore.BLUE + Style.BRIGHT + 'É um número PAR entre 0 a 30')
        elif 30 > numero <= 60 and numero % 2 == 0:
            print(Fore.BLUE + Style.BRIGHT + 'É um número PAR entre 30 a 60')
        elif 60 > numero <= 100 and numero % 2 == 0:
            print(Fore.BLUE + Style.BRIGHT + 'É um número PAR entre 60 a 100')

        elif numero <= 30 and numero % 2 == 1:
            print(Fore.BLUE + Style.BRIGHT + 'É um número IMPAR entre 0 a 30')
        elif 30 > numero <= 60 and numero % 2 == 1:
            print(Fore.BLUE + Style.BRIGHT + 'É um número IMPAR entre 30 a 60')
        elif 60 > numero <= 100 and numero % 2 == 1:
            print(Fore.BLUE + Style.BRIGHT + 'É um número IMPAR entre 60 a 100')

    if per > numero:
        sleep(0.5)
        print(Fore.GREEN + Style.BRIGHT + 'Você PASSOU do número escolhido, cotinue tentando')
        sleep(0.5)
        print()
        cont += 1
    if per < numero:
        sleep(0.5)
        print(Fore.GREEN + Style.BRIGHT + 'O número está ADIANTE, continue tentando')
        sleep(0.5)
        print()
        cont += 1
print(Fore.MAGENTA + f'PARABÉNS! o número escolhido foi o {numero} \nFIM, Obrigado por jogar!')