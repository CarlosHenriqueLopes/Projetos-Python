"""
Calculando viagem
Até 200 km pagar 0.50 centavos e 0.45 centavos para viagens acima de 200km
"""

from time import sleep

def titulo(t):
    print('=' * 25)
    print(t.center(25))
    print('=' * 25)


titulo('CALCULANDO DISTANCIA')
sleep(0.5)
print('Até 200km/h para R$0.50 por km')
print('Acima de 200km/h para R$0.45 por km')
sleep(1)
print()
dis = int(input('Digite a distancia da viagem: '))
sleep(0.5)

if dis <= 200:
    valor = 0.50 * dis
    print(f'O proço da viagem vai custar R${valor:.2f}')
else:
    valor = 0.45 * dis
    print(f'O proço da viagem vai custar R${valor:.2f}')