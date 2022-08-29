# Meta caracteres: . ^ * + ? { } [ ] \ | ( )
# | -> ou
# . ->  Retorna qualquer caracter (menos que tenha quebra de linha)
# [] -> Conjustos de caracteres

import re
from tkinter.messagebox import IGNORE

texto = '''
Carlos, carlos
Escrevendo um texto para testar a lib (biblioteca) re do python.
Escrevendo palavras repitidas também. Escrevendo palavras repitidas também.
Palavra com vraaaaaaaariaaaaaas letras
'''

# | -> ou
# Para achar mais de uma palavra usar o caracter | (serve como OU)
print(re.findall(r'Escrevendo|palavras', texto))

''' 
Retorna uma lista na ordem das palavras
-> ['Escrevendo', 'Escrevendo', 'palavras', 'Escrevendo', 'palavras']
'''


#--------------------------------------------------------------------


# . ->  Retorna qualquer caracter (menos que tenha quebra de linha)
# O ponto substitue caracterers
print(re.findall(r'Escrevendo|palavras|rep..idas', texto))
# Retorna uma lista na ordem das palavras


#--------------------------------------------------------------------


# [] -> Conjustos de caracteres
print(re.findall(r'[Cc]arlos', texto))
# Exemplo abrangendo mais letras
print(re.findall(r'[Ccabcde]arlos', texto))
print(re.findall(r'[A-Z]arlos', texto))
print(re.findall(r'[a-z]arlos', texto))
print(re.findall(r'[A-Z a-z]arlos', texto))
print(re.findall(r'[A-Z a-z 0-9]arlos', texto))
# Também é possivél usar entra as palavras


#--------------------------------------------------------------------


# Ignorar caracterres diferestes
# flags=
print(re.findall(r'CaRlOs|eScReVenDo', texto, flags=re.IGNORECASE))
# Retorna uma lista na ordem das palavras


#--------------------------------------------------------------------

palavras = re.compile(r'Escrevendo|Carlos')
print(palavras.findall(texto))


palavras_2 = re.compile(r'[A-z a-z]arlos')
print(palavras_2.findall(texto))