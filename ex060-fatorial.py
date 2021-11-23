from math import prod
from time import sleep
cores = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'verde':'\033[1:32m',
         'amarelo': '\033[1:33m',
         'negrito': '\033[1m',
         'cls': '\033[m'}
print(f'{cores["amarelo"]}-={cores["cls"]}' * 20)
print(f"{cores['azul']}{'FATORIAL':^40}{cores['cls']}")
print(f'{cores["amarelo"]}-={cores["cls"]}' * 20)
num = int(input('Digite um número inteiro: '))
count = num
f = 1
print(f'Calculando {num}!: ', end='')
while count > 0:
    sleep(0.5)
    print(f'{count}', end='')
    sleep(0.5)
    print(' x ' if count > 1 else ' = ', end='')
    f *= count
    count -= 1
print(f)

'''fat = []
n = num
while n != 0:
    fat.append(n)
    n = n - 1
print(f'O FATORIAL DE {cores["azul"]}{num}{cores["cls"]} É: {cores["azul"]}{prod(fat)}{cores["cls"]}')'''
