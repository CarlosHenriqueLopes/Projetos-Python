"""
calculo usado para achar a idade: data atual - ano de nascimento = idade
calculo usando para achar o ano de aposentadoria (35anos): (ano de contratação + 35) - ano de nascimento

linha 10: comando para pegar o ano atual da maquina
linha 15: pegar o ano de nascimento para achar a idade e colocar no dict()
linha 22: pegando o salário
linha 23: trocando a pontuação da formatação usando .replace()
"""

from time import sleep
from datetime import date
atual_dt = date.today().year

dados = dict()

print('O cadastro vai pedir nome, idade e CTPS (carteira de trabalho)')
print('Caso não tenha digitar 0 (zero) para continuar e finalizar a operação')
print()
sleep(0.5)
dados['Nome'] = str(input('Digite o nome: '))
nascimento = int(input('Digite o ano de nascimento: '))
idade = atual_dt - nascimento
dados['Idade'] = idade
dados['CTPS'] = int(input('Número da carteira de trabalho (0 p/ñ): '))
if dados['CTPS'] != 0:
    dados['Ano contratação'] = int(input('Digite o ano de contratação: '))
    salario = float(input('Digite o salário: '))
    valor = f'{salario:.2f}'.replace(',', '_').replace('.', ',').replace('_', '.')
    dados['Salário'] = f'R${valor}'
    dados['Aposentadoria'] = f'{(dados["Ano contratação"] + 35) - nascimento} anos'

print()
sleep(0.5)
for k, v in dados.items():
    print(f'{k} - {v}')