
## Revolser o problema da cobrinha não responder o direcional ##

import pygame
from random import randint
from pygame.locals import *

pygame.init()

# setando uma diração fixa
direcao = K_LEFT

tamanho_tela = (600, 600)
janela = pygame.display.set_mode((tamanho_tela))
pygame.display.set_caption('Jogoda da Cobrinha')

# eixo (X,Y)
cobrinha = [(250, 50), (260, 50), (270, 50)]
# .Surface desenhar muitas imagens em outra (10,10 quadrado)
skin = pygame.Surface((10, 10))
# .fill cores RGB
skin.fill((144, 238, 144))

#gerando posição aleatoria de 0 a 590 (590 pq os quadrinhos são de tamanho 10, 590 é o ultimo lugar sem sair da tela)
maca_pos = (randint(0, 600), randint(0, 600))
# .Surface desenhar muitas imagens em outra (10,10 quadrado)
maca = pygame.Surface((10, 10))
# .fill cores RGB
maca.fill((255, 0, 0))

#.time.Clock criar um objeto para ajudar a controlar o tempo
# para setar um tempo para que a cobrinha não ande muito rápido
relogio = pygame.time.Clock()

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

## terminar essa parte depois que fazer a cobrinha responder o direcional ##
def restart():
    cobrinha = [(250, 50), (260, 50), (270, 50)]
    maca_pos = (randint(0, 600), randint(0, 600))
    direcao = K_LEFT
#-----------------------------------------------------

rodando = True
while rodando:
    # tempo de movimento da cobrinha
    relogio.tick(10)

    # comando .fill para limpar a tela, pq ela vai ficar sendo atualizada (RGB 0,0,0)
    janela.fill((0,0,0))

    for c in pygame.event.get():
        if c.type == pygame.QUIT:
            rodando = False

        # se uma tecla for precionada
        elif c.type == KEYDOWN:
            if c.type in [K_UP, K_DOWN, K_LEFT, K_RIGHT]:
                direcao = c.type


    # .blit desenhar uma imagem sobre outra
    janela.blit(maca, maca_pos)

    #comando a maça
    if colisao(maca_pos, cobrinha):
        cobrinha.append((0,0))
        maca_pos = maca_pos

    # Comando for para mover o cabeça:
    # usando o comando for, pq a snake são variás tuplas
    for pos in cobrinha:
        # para cada posição da cobrinha
        # .blit para senhar uma img sobre a outra
        janela.blit(skin, pos)

    # Comando for para mover o corpo:
    # o corpo vai ocupando o lugar da cabela para ela andar
    # setando o range: -1 pq começa do final, 0 não é incluso, -1 para ir diminuindo
    for corpo in range(len(cobrinha) - 1, 0, - 1):
        if colisao(cobrinha[0], cobrinha[corpo]): # def colisao está passando por td corpo da cobrinha
            pygame.quit()
            quit()
        cobrinha[corpo] = cobrinha[corpo - 1]

    if direcao == K_UP:
        # posição da cabela = posX, posY - 10 (Y - 10 pq está indo para cima)
        cobrinha[0] = (cobrinha[0][0], cobrinha[0][1] - 10)
    elif direcao == K_DOWN:
        # posição da cabela = posX, posY - 10 (Y + 10 pq está indo para baixo)
        cobrinha[0] = (cobrinha[0][0], cobrinha[0][1] + 10)
    elif direcao == K_RIGHT:
        # posição da cabela = posX, posY - 10 (X + 10 pq está indo para direita)
        cobrinha[0] = (cobrinha[0][0] + 10, cobrinha[0][1])
    elif direcao == K_LEFT:
        # posição da cabela = posX, posY - 10 (X - 10 pq está indo para esquerda)
        cobrinha[0] = (cobrinha[0][0] - 10, cobrinha[0][1])

    # se a cabeça sair dos limites, quita
    if limite_tela(cobrinha[0]):
        pygame.quit()
        quit()

    pygame.display.update()
