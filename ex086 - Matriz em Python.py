#   Crie um programa que declare uma matriz de dimensão 3×3
#   e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela,
#   com a formatação correta.

#   Cabeçalho apenas para efeitos visuais
cores = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'verde':'\033[1:32m',
         'amarelo': '\033[1:33m',
         'negrito': '\033[1m',
         'cls': '\033[m'}
print(f'{cores["amarelo"]}-={cores["cls"]}' * 25)
print(f"{cores['verde']}{'MATRIZ EM PYTHON':^50}{cores['cls']}")
print(f'{cores["amarelo"]}-={cores["cls"]}' * 25)

#   Início do programa
matriz = [[], [], []]
for lc in range(3):
    matriz[lc] = [0] * 3
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'DIGITE UM VALOR PARA {[l, c]}: '))
print('-' * 50)
for linha in matriz:
    for num in linha:
        print(f'[{num:^6}]', end='')
    print()
