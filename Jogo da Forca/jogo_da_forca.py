from boneco import *
from defs import *
import random
from time import sleep

lista = ['github', 'notebook', 'python', 'html', 'css', 
'programador', 'mouse', 'teclado', 'computador', 'javascript', 'javascript']


sorteio = random.choice(lista)
print(sorteio) # -> Lembrete: usar só para testar os comandos
acertos = 0
erros = 0
letras_ac = ' '
letras_er = ' '

titulo('JOGO DA FORCA')
print('Jogo da forca com 11 palavras aleatorias reçacionadas a T.I.')
print('Voçê tem 6 tentativas para acertar a letra')

while acertos != len(sorteio) and erros != 6:
    per = str(input('\nDigite uma letra: ')).lower().strip()

    # para ver letras repetidas
    if per in letras_ac + letras_er:
        resp = 'Você já digitou essa letra. Tente outra'
        print(cor('roxo', resp))
        continue

    if per in sorteio:
        resp = 'PARABÉNS você acertou uma letra'
        print(cor('azul', resp))
        acertos += sorteio.count(per)
        letras_ac += per
    else:
        resp = 'ERROU. Tente denovo'
        print(cor('vermelho', resp))
        erros += 1
        letras_er += per

    sleep(0.5)
    print(forca + boneco[erros])
    titulo('Situação da palavra')
    for c in sorteio:
        if c in letras_ac:
            print(f'{c} ', end='')
        else:
            print('_ ', end='')
    print()

print()
sleep(1)
fim = 'FIM, OBRIGADO POR JOGAR'
print(f'\n{cor("cf", fim)}')