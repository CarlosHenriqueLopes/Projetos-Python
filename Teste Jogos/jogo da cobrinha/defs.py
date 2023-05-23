#gerando posição aleatoria da maça de 0 a 600
def maca_grid():
    x = randint(0, tamanho_tela[0])
    y = randint(0, tamanho_tela[1])
    # Sempre que n tiver um multiplo de 10,
    # arredonda para baixo,
    # por causa do tamanho do pixel da cobrinha q é 10
    return x // 10 * 10, y // 10 * 10
maca_pos = maca_grid()

# se uma posição for igual a outra == colisao
def colisao(pos1, pos2):
    return pos1 == pos2

def limite_tela(pos):
    # menor ou igual a 0, ou menor que o tamanho maximo (eixo X,Y)
    # Flase dentro, True fora
    if 0 <= pos[0] < tamanho_tela[0] and 0 <= pos[1] < tamanho_tela[1]:
        return False
    else:
        return True


# para não chamar as variaveis dnv, usar esta function
def restart():
    global cobrinha
    global maca_pos
    global direcao
    cobrinha = [(250, 50), (260, 50), (270, 50)]
    maca_pos = maca_pos
    direcao = K_LEFT
