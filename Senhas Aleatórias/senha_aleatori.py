import string
from random import SystemRandom

# random.choices(sequence, weights=None, cum_weights=None, k=1)

# sequence
# Requeridos. Uma sequência como uma lista, uma tupla, um intervalo de números etc.

# weights
# Opcional. Uma lista onde você pode pesar a possibilidade para cada valor.
# Padrão Nenhum

# cum_weights
# Opcional. Uma lista onde você pode pesar a possibilidade para cada valor, só que desta vez a possibilidade é acumulada.
# Exemplo: lista de pesos normais: [2, 1, 1] é o mesmo que esta lista cum_weights; [2, 3, 4].
# Padrão Nenhum

letras = string.ascii_letters # -> pegas todas as letras da lib
pontuação = string.punctuation # -> pegar toda as pontuações das lib
letra_pont = letras + pontuação # -> contatenação

senha = ''.join(SystemRandom().choices(letra_pont, k=6)) # -> k quantidade de numeros

print(senha)