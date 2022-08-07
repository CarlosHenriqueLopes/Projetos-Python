"""
Resumo: Se o valor for >= a cadula máxima, vai diminuindo pela cédula maior até não dar mais,
depois ir diminuindo por cédulas menores com o mesmo processo.

"""


cedula = 100
total_cedula = 0

valor = int(input('Quando você quer sacar? '))
print()
while True:
    if valor >= cedula:
        valor -= cedula
        total_cedula += 1
    else:
        if cedula > 0:
            print(f'Seu saque será de {total_cedula} cédulas de {cedula}')
        if cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 2
        total_cedula = 0
        
        if valor == 0:
            break

print('Fim do precesso')