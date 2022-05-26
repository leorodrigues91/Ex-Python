cores = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'verde':'\033[1:32m',
         'amarelo': '\033[1:33m',
         'negrito': '\033[1m',
         'cls': '\033[m'}
print(f'{cores["amarelo"]}-={cores["cls"]}' * 15)
print(f"{cores['verde']}{'TABUADA':^30}{cores['cls']}")
print(f'{cores["amarelo"]}-={cores["cls"]}' * 15)
n = int(input('Digite um número para ver sua tabuada: '))
print(f'A tabuada de {n} é:')
print('-' * 15)
for mult in range(1, 11):
    print(f'{n:3} x {mult:2} = {n * mult:2}')
print('-' * 15)
