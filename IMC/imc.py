# 1º Método:

def IMC(peso, altura):
    a = altura ** 2
    b = peso / a
    return round(b)
    

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

print(IMC(peso, altura))
# --------------------------------------------------------------------------------------------------------------

# 2º Método:
# Fazendo o uso do eval()

peso = eval(input("Digite seu peso: "))
altura = eval(input("Digite sua altura: "))

imc = peso/(altura ** 2)

print(f"Seu IMC é {imc}")