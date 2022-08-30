# Meta caracteres quantificadores: . ^ * + ? { } [ ] \ | ( )

# * -> 0 (precisa existir) ou ilimitadas repetições
# + -> 1 ou ilimitadas repetições
# ? -> 0 ou 1 (pode ou não existir)
# {n quantidades de repetições}
# {min, max} 
# . ->  Retorna qualquer caracter (menos que tenha quebra de linha)

import re

texto = '''
<p> Frase1 </p>  <p> Frase2 </p>  <p> Frase3 </p>  <p> Frase4 </p>  <div> Frase na div </div>
'''

#(grid = gulozo)

# primeiras tags <[pdiv]{1,3}
# fecamento delas <\/[pdiv]{1,3}>

# pegando as primeiras tags
# uma letra (p), tres letras (div)
print(re.findall(r'<[pdiv]{1,3}', texto))

# pegando tudo usando o ponto all
# # . -> (qualquer caracter) * (all)
print(re.findall(r'<[pdiv]{1,3}.*', texto))

# concatenando com as tags de fechamento
# mesmo principio -> (<\/>[pdiv]{1,3})
print(re.findall(r'<[pdiv]{1,3}.*<\/[pdiv]{1,3}>', texto))


#(não grid)

# ? -> 0 ou 1 (pode ou não existir)
# a ? vai ver onde começa e quando encontrar onde já pode terminar, ele entrar
print(re.findall(r'<[pdiv]{1,3}.*?<\/[pdiv]{1,3}>', texto))