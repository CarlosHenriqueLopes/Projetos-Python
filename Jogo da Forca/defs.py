def titulo(t):
    print('=' * 30)
    print(f'\033[1;36m{t.center(30)}\033[m')
    print('=' * 30)


# OBS: Colorindo utilizando o modo de programação ANSI (por caracteres)
def cor(x, n):
    if x == 'azul':
        return f'\033[1;36m{n}\033[m'
    if x == 'vermelho':
        return f'\033[1;31m{n}\033[m'
    if x == 'roxo':
        return f'\033[1;35m{n}\033[m'
    if x == 'cf':
        return f'\033[1;7;40m{n.center(30)}\033[m'