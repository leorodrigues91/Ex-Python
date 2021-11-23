from random import randint
cores = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'verde':'\033[1:32m',
         'amarelo': '\033[1:33m',
         'negrito': '\033[1m',
         'cls': '\033[m'}
print(f'{cores["amarelo"]}-={cores["cls"]}' * 25)
print(f"{cores['verde']}{'MAIOR MENOR EM LISTA':^50}{cores['cls']}")
print(f'{cores["amarelo"]}-={cores["cls"]}' * 25)
num = []
maior = menor = 0
for c in range(0, 5):
    n = int(input(f'DIGITE UM VALOR PARA A POSIÇÃO {c}: '))
    num.append(n)
    if c == 0:
        maior = menor = num[c]
    else:
        if num[c] > maior:
            maior = num[c]
        if num[c] < menor:
            menor = num[c]
print('-' * 50)
print(f'Os valores digitados foram: {num}')
print(f'O maior valor é {maior} nas posições: ', end=' ')
for ind, valor in enumerate(num):
    if valor == maior:
        print(f'{ind}... ', end='')
print()
print(f'O menor valor é {menor} nas posições: ', end=' ')
for ind, valor in enumerate(num):
    if valor == menor:
        print(f'{ind}... ', end='')
print()
#print(f'O maior valor é {max(num)} na posição {num.index(max(num))}')
#print(f'O menor valor é {min(num)} na posição {num.index(min(num))}')
