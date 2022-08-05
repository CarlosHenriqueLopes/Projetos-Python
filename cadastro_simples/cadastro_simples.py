"""
O programa vai ler idade e sexo de varias pessoas e dizer:
Quantas PESSOAS TEM MAIS DE 18 ANOS, quantidade de HOMENS CADASTRADOS e MULHERES COM MENOS DE 20 ANOS
"""
from time import sleep

cont = homens = mulheres = 0

while True:
    idade = int(input('Digite a idade: '))
    sleep(0.5)
    if idade > 18:
        cont += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo (M/F): ')).upper().strip()[0]
        sleep(0.5)
        if sexo == 'M':
            homens += 1
        if sexo == 'F' and idade < 20:
            mulheres += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Cadastrar mais pessoas? ')).upper().strip()[0]
        sleep(0.5)
    if continuar == 'N':
         break

sleep(1)
print('\n')
print(f'Pessoas com mais de 18 anos cadastradas: {cont}\n')
print(f'Quantidade de homens cadastrados: {homens}\n')
print(f'Quantidade de mulheres com menos de 20 anos cadastradas: {mulheres}\n')
