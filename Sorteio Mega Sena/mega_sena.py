import random
from time import sleep

numeros_mega = list()
lista_escolha = list()

print('Escolha 6 números de 1 a 60 para o sorteio da mega: ')
sleep(0.3)
print()


# coletar os 6 números do usuario, e adicionar em uma lista
# (usando o comando for)

#for c in range(1, 7):
#    n = int(input(f'{c}º: '))
#    lista_escolha.append(n)


#( usando o comando while)
cont = 1
while cont != 7:
    n1 = int(input(f'{cont}º: '))
    lista_escolha.append(n1)
    cont += 1
print()
# print(lista_escolha) # -> mostrar os valores do usuario na lista, para teste


# coletar os números da mega sena, que vai de 1 a 60, e adicionar em outra lista
for c in range(1, 61):
    numeros_mega.append(c)
#print(numeros_mega) # -> mostrar os números da mega na lista, para teste


random.shuffle(numeros_mega)
premio = numeros_mega[0:6]

if premio == lista_escolha:
    print(f'Resultados do sorteio da Mega Sena: {premio}')
    sleep(1)
    print('PARABÉNS VOCÊ GANHOU O PRIMEIO DA MEGA SENA!!!!')
else:
    print(f'Resultados do sorteio da Mega Sena: {premio}')
    sleep(1)
    print(f'Você não ganhou o premio, sua escolha de números {lista_escolha}')