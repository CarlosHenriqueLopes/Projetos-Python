import re

# findall, search, sub, compile

# OBS: sempre que digitar expreções regulares usa o r'' (érre), para # evitar de digitar barr invertida

paravra_string = 'Teste com expreções regulares, colocando mais palavras aletatorias expreções para testes'
'''
# Para saber se a paralavra existe dentro da frase
print(re.search(r'expreções', paravra_string))
#RETORNO -> <re.Match object; span=(10, 19), match='expreções'>

# ----------------------------------------------------------------------------

# Para encontrar TODAS as OCORRENCIAS dentro da frase
print(re.findall(r'expreções', paravra_string))
# RETORNO -> uma lista com todas as ocorrencias ['expreções']

# ----------------------------------------------------------------------------

# Para substituir todas as ocorrencias
print(re.sub(r'expreções', 'TROCA_DE_PARAVA', paravra_string))
# RETORNO -> Teste com TROCA_DE_PARAVA regulares

# parametro count=n para qtdd de valores que for substituir (parametro padrão count=0)
print(re.sub(r'expreções', 'TROCA_DE_PARAVA', paravra_string, count=1))

# ----------------------------------------------------------------------------
'''
armazenar = re.compile(r'expreções')

print(armazenar.search(paravra_string))
print(armazenar.findall(paravra_string))
print(armazenar.sub('TROCA_DE_PARAVA', paravra_string))
print(armazenar.sub('TROCA_DE_PARAVA', paravra_string, count=1))