## Exempli simples de como fazer cadastro de pessoas utilizando classes
## O cadastro trabalha com duas classes, Cliente para adicionar o nome, CPF e idade
## e Conta para adicionar um cliente (no caso adicona a primeira classe, já com a função __str__ para mostrar td o conteuro)
## e um saldo

from classes import *


cliente1 = Cliente("Carlos", "123.456.789.01", 30)
# Aqui consigo mostrar todos os dados da classe Cliente de uma só vez printando cliente1, por causa da def __str__
print(cliente1)
print()

# Em cliente adiciono o cliente.nome (pegando só o nome), e o saldo da conta
# Também é possível mostrar toda a classe Conta só com o print da classe, por causa da def __str__
conta_Carlos = Conta(cliente1.nome, 200.000)
print(conta_Carlos)

conta_Carlos.soma(100.000)
print(conta_Carlos)
print("-------------------------------------------------------------")


cliente2 = Cliente("Henrique", "123.345.567.77", 31)
print(cliente2)
print()

conta_Henrique = Conta(cliente2.nome, 300.00)
print(conta_Henrique)

conta_Henrique.soma(100.000)
print(conta_Henrique)