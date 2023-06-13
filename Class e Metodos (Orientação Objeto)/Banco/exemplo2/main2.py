## No exemplo 2 tem o funcionamento parecido com o primeiro, mais utilizando a def __str__só na primeira classe
## facilitando a manipulação pela classe Conta, e deixando o cógigo mais limpo nas chamadas
## e acrescentei uma logica mais elabora da função de saque.
## Quando o saque ultrapassar a quantide maxima definida pelo usuário, o valor será descontado do limite, se possível

from classes2 import *

cliente1 = Cliente("Carlos", "123.456.789.01", 30)
# Aqui consigo mostrar todos os dados da classe Cliente de uma só vez printando cliente1, por causa da def __str__
# print(cliente1)


# Setando a classe Conta
conta_Carlos = Conta(cliente1, 1000, 3000)

# A classe Cliente returna tds os dados, e foi adicionado em cliente da classe Conta
# Por isso ao chamar o metetodo cliente retorna tds os dados
print(conta_Carlos.cliente)

# Agora nome também está no metodo cliente (assim como CPF e idade)
print(conta_Carlos.cliente.nome)
print(conta_Carlos.cliente.CPF)
print(conta_Carlos.cliente.idade)
print()

# Mostrando o saldo
print(conta_Carlos.saldo)
# Foi feito uma condição para no caso de adicionar 0
print(conta_Carlos.soma(0))
print(conta_Carlos.soma(1000))
print(conta_Carlos.ver_saldo())
print()

print(conta_Carlos.sacar(500))
print(conta_Carlos.ver_saldo())
print()

# Mostrando limite
print(conta_Carlos.consultar_limite())
print(conta_Carlos.aumentar_limite(1000))
print(conta_Carlos.consultar_limite())
print()

print(conta_Carlos.sacar(1000))
print(conta_Carlos.ver_saldo())
print(conta_Carlos.sacar(1000))