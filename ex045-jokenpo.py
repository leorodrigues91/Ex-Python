from random import randint
from time import sleep
cores = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'verde':'\033[1:32m',
         'amarelo': '\033[1:33m',
         'negrito': '\033[1m',
         'cls': '\033[m'}
itens = ('PEDRA', 'PAPEL', 'TESOURA')
pc = randint(0, 2)
print(f'{cores["amarelo"]}-={cores["cls"]}' * 15)
print(f"{cores['verde']}{'JOKENPÔ':^30}{cores['cls']}")
print(f'{cores["amarelo"]}-={cores["cls"]}' * 15)
print(f'{cores["red"]}Será que você consegue me vencer?{cores["cls"]}')
print(f'Escolha uma das opções abaixo para jogar:\n'
      f'- {cores["azul"]}0{cores["cls"]} para {cores["amarelo"]}pedra{cores["cls"]};\n'
      f'- {cores["azul"]}1{cores["cls"]} para {cores["amarelo"]}papel{cores["cls"]};\n'
      f'- {cores["azul"]}2{cores["cls"]} para {cores["amarelo"]}tesoura{cores["cls"]}.')
jogador = int(input('Digite aqui a sua jogada: '))
if jogador == 0 or jogador == 1 or jogador == 2:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!!')
    sleep(1)
    print('-' * 20)
    print(f'A MÁQUINA JOGOU: {itens[pc]}')
    print(f'VOCÊ ESCOLHEU: {itens[jogador]}')
    print('-' * 20)
    if pc == 0:  # maquina jogou pedra
        if jogador == 0:  # pedra
            print(f'{cores["amarelo"]}EMPATE{cores["cls"]}')
        elif jogador == 1:  # papel
            print(f'{cores["verde"]}VOCÊ VENCEU!!{cores["cls"]}')
        elif jogador == 2:  # tesoura
            print(f'{cores["red"]}A MÁQUINA VENCEU!{cores["cls"]}')
    if pc == 1:  # maquina jogou papel
        if jogador == 0:  # pedra
            print(f'{cores["red"]}A MÁQUINA VENCEU!{cores["cls"]}')
        elif jogador == 1:  # papel
            print(f'{cores["amarelo"]}EMPATE{cores["cls"]}')
        elif jogador == 2:  # tesoura
            print(f'{cores["verde"]}VOCÊ VENCEU!!{cores["cls"]}')
    if pc == 2:  # maquina jogou tesoura
        if jogador == 0:  # pedra
            print(f'{cores["verde"]}VOCÊ VENCEU!!{cores["cls"]}')
        elif jogador == 1:  # papel
            print(f'{cores["red"]}A MÁQUINA VENCEU!{cores["cls"]}')
        elif jogador == 2:  # tesoura
            print(f'{cores["amarelo"]}EMPATE{cores["cls"]}')
else:
    print(f'{cores["red"]}JOGADA INVÁLIDA!!{cores["cls"]}')