

from cgitb import grey
import pygame
pygame.init()


janela = pygame.display.set_mode((800, 600)) # -> Para definir o tamanho da janela em pixels)
pygame.display.set_caption('Jogo da bolinha com Python') # -> Para adicionar um nome em cima da janela

#posição no centro
x = 400
y = 300
velocidade = 15 #pixel

# para manter a janela aberta até que o usuario a feche
jaela_aberta = True
while jaela_aberta:

    pygame.time.delay(50) # -> (mile segundos) criar um delay para executar essa parte do programa

    for c in pygame.event.get(): # -> avita essa condição quando rodar um evento
        if c.type == pygame.QUIT:
            jaela_aberta = False
        
    #Para quando precionar uma tecla (key) executar uma ação (para os movimentos)
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        y -= velocidade
    if comandos[pygame.K_DOWN]:
        y += velocidade
    if comandos[pygame.K_RIGHT]:
        x += velocidade
    if comandos[pygame.K_LEFT]:
        x -= velocidade

    janela.fill((000, 000, 000))
    # .draw para criar um circulo (paremetros: cor, posição, raio do circulo)
    pygame.draw.circle(janela, (0,200,210), (x, y), 50)

    pygame.display.update() # -> Para atualizar

pygame.quit()