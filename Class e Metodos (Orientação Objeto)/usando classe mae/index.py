from classes import *

veiculo_classeMae = Veiculo("cinza", "ford", 10, 1000)
print(veiculo_classeMae.cor)
print(veiculo_classeMae.marca)
print(veiculo_classeMae.roda)
print(veiculo_classeMae.tanque)
print()

#------------------------------------------------------------------------------

# o carro já vem com a quantidade de rodas definidas
carro = Carro("branco", "Porche", 10)
print(carro.cor)
print(carro.marca)
print(carro.roda)
print(carro.tanque)

carro.abastecer(30) # somando mais litros
print(carro.tanque)

carro.abastecer(100) # aqui cai no limite de quantidade, e retorna o False
print(carro.tanque)

print()
#------------------------------------------------------------------------------

# tb com quantidade de rodas definidas
moto = Moto("preta", "Yamaha", 20)
print(moto.cor)
print(moto.marca)
print(moto.roda)
print(moto.tanque)

moto.abastecer(30)
print(moto.tanque)

moto.abastecer(100)
print(moto.tanque)

print()
#------------------------------------------------------------------------------

# tb com quantidade de rodas definidas
caminhao = Caminhao("verde", "BMW", 100)
print(caminhao.cor)
print(caminhao.marca)
print(caminhao.roda)
print(caminhao.tanque)

caminhao.abastecer(20)
print(caminhao.tanque)

caminhao.abastecer(1000)
print(caminhao.tanque)