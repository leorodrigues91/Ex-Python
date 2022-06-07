#   Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#   O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
#   entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

#   CABEÇALHO APENAS PARA EFEITOS VISUAIS
cores = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'verde':'\033[1:32m',
         'amarelo': '\033[1:33m',
         'negrito': '\033[1m',
         'cls': '\033[m'}
print(f'{cores["amarelo"]}-={cores["cls"]}' * 25)
print(f"{cores['verde']}{'MATRIZ EM PYTHON - APRIMORADO':^50}{cores['cls']}")
print(f'{cores["amarelo"]}-={cores["cls"]}' * 25)

#   INÍCIO DO PROGRAMA
from time import sleep
from random import randint

p = int(input('QUANTOS JOGOS VOCÊ DESEJA SORTEAR? '))
print(f'{f" SORTEANDO {p} JOGOS ":-^50}')
sleep(1)
for n in range(p):
    jogos = []
    while len(jogos) != 6:
        num = randint(1, 60)
        if num not in jogos:
            jogos.append(num)
    jogos.sort()
    print(f' JOGO {n+1}: {jogos}')
    jogos.clear()
    sleep(1)
print(f'{f" < BOA SORTE!! > ":-^50}')
