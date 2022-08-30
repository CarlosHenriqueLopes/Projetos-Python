# Meta caracteres quantificadores: . ^ * + ? { } [ ] \ | ( )

# * -> 0 (precisa existir) ou ilimitadas repetições
# + -> 1 ou ilimitadas repetições
# ? -> 0 ou 1 (pode ou não existir)
# {n quantidades de repetições}
# {min, max} 

import re

texto = '''
Carlos, carlos
Escrevendo um texto para testar a lib (biblioteca) re do python.
Escrevendo palavras repitidas também. Escrevendo palavras repitidas também.
Palavra com vaaaaaaaariaaaaaas letras
'''

texto_2 = '''
Outras palavra para testes: Veeemm, veem, veeem, vemm.
Frase com palavras parecidas para exemplo: Quam não ama ser amado, Ama ser Amado
'''

# + -> 1 ou ilimitadas repetições
# {min,max}
# {,10} 0 a 10
# {10,} 10 a 0
# {10} especifico 10

print(re.findall(r'va+rias', texto, flags=re.IGNORECASE))
# caso não for, retorna uma lista vazia -> []



print(re.findall(r'va+ria+s', texto, flags=re.IGNORECASE))
# --------------------------------------------------------------------
print(re.findall(r'va{1,}ria{1,}s', texto))
# returorna com todos os caracteres -> ['vaaaaaaaariaaaaaas']
# --------------------------------------------------------------------
# pegando uma palavra que tenha 3 e (letra e) e 2 m (letra m )
print(re.findall(r've{3}m{1,2}', texto_2, flags=re.IGNORECASE))



print(re.findall(r'va+ria|carlos', texto, flags=re.IGNORECASE))
# se os caracteres forem iguais -> ['vaaaaaaaaria']

# --------------------------------------------------------------------

# Também usando os dois metodos para o sub (para substituir)
# Para substituir todos os caracteres apresentados

print(re.sub(r'va+ria+s|Carlos', 'ABC', texto, flags=re.IGNORECASE))
print(re.sub(r'va{1,}ria{1,}s|Carlos', 'ACB', texto, flags=re.IGNORECASE))

# --------------------------------------------------------------------


# Usando o quantificador com conjustos
# Pegando duas vezes os caracteres que se encaixam na busca
print(re.findall(r'ama[a-z]*', texto_2, flags=re.IGNORECASE))
print(re.findall(r'ama[do]{,2}', texto_2, flags=re.IGNORECASE))
# {min,max}
# retornando [ama, amado, Ama, Amado]

# Só a palavra que se encaixa na busca
print(re.findall(r'ama[a-z]+', texto_2, flags=re.IGNORECASE))
print(re.findall(r'ama[do]{2}', texto_2, flags=re.IGNORECASE))
print(re.findall(r'ama[do]{1,2}', texto_2, flags=re.IGNORECASE))
print(re.findall(r'ama[do]{0,2}', texto_2, flags=re.IGNORECASE))
print(re.findall(r'ama[do]+', texto_2, flags=re.IGNORECASE))
# returnado [amado, Amado]
