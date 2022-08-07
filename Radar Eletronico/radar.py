"""
Radar eletronico
Limite: 80km/h
valor: R$7.00
"""

from time import sleep

def titulo(t):
    print('=' * 25)
    print(t.center(25))
    print('=' * 25)

    
titulo('RADAR ELETRONICO')
velocidade = int(input('Digite a velocidade: '))
sleep(0.5)
print()
if velocidade > 80:
    multa = (velocidade - 80) * 7
    limite = velocidade - 80
    print(f'Você ecedeu o limite de velocidade em {limite}km/h, e irá pagar uma multa de R${multa:.2f}')
else:
    print('Você está dentro do limite de velocidade')
print()
print('FIM')