

from turtle import left
import pygame
from random import randint

pygame.init()

x = 600
y = 600
cima = 0
direita = 1
baixo = 2
esquerda = 3

janela = pygame.display.set_mode((x, y))
pygame.display.set_caption('Jogoda da Cobrinha')
cobrinha = [(200, 200), (210, 200), (220, 200)]
direção = esquerda

skin = pygame.Surface((10, 10))
skin.fill((200, 100, 200))

maça_posição = (randint(0, 590), randint(0, 590))
maça = pygame.Surface((10, 10))
maça.fill((255, 0, 0))

relogio = pygame.time.Clock()

rodando = True
while rodando:
    relogio.tick(20)

    for c in pygame.event.get():
        if c.type == pygame.QUIT:
            rodando = False

    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        y -= direção
    if comandos[pygame.K_DOWN]:
        y += direção
    if comandos[pygame.K_RIGHT]:
        x += direção
    if comandos[pygame.K_LEFT]:
        x -= direção


    if direção == cima:
        cobrinha[0] = (cobrinha[0][0], cobrinha[0][1] - 10)
    if direção == baixo:
        cobrinha[0] = (cobrinha[0][0], cobrinha[0][1] + 10)
    if direção == direita:
        cobrinha[0] = (cobrinha[0][0] + 10, cobrinha[0][1])
    if direção == esquerda:
        cobrinha[0] = (cobrinha[0][0] - 10, cobrinha[0][1])

    for corpo in range(len(cobrinha) - 1, 0, - 1):
        cobrinha[corpo] = (cobrinha[corpo - 1][0], cobrinha[corpo - 1][0])

    janela.fill((0,0,0))
    janela.blit(maça, maça_posição)
    for pos in cobrinha:
        janela.blit(skin, pos)


    pygame.display.update()