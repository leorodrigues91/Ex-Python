from random import randint
cores = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'verde':'\033[1:32m',
         'amarelo': '\033[1:33m',
         'negrito': '\033[1m',
         'cls': '\033[m'}
print(f'{cores["amarelo"]}-={cores["cls"]}' * 25)
print(f"{cores['verde']}{'TUPLA SORTEIO':^50}{cores['cls']}")
print(f'{cores["amarelo"]}-={cores["cls"]}' * 25)
'''num = []
cont = 1
while cont <= 5:
    n = randint(0, 10)
    num.append(n)
    cont += 1
tupla = (num)
num = sorted(num)
maior = num[-1]
menor = num[0]'''
num = (randint(0, 10), randint(0, 10), randint(0, 10),
       randint(0, 10), randint(0, 10))
print(f'OS VALORES SORTEADOS FORAM: {", ".join(map(str, num))}')
print('-' * 50)
print(f'O MAIOR VALOR SORTEADO FOI {max(num)}\n'
      f'O MENOR VALOR SORTEADO FOI {min(num)}')
