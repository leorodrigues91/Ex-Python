cores = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'verde':'\033[1:32m',
         'amarelo': '\033[1:33m',
         'negrito': '\033[1m',
         'cls': '\033[m'}
print(f'{cores["amarelo"]}-={cores["cls"]}' * 20)
print(f"{cores['verde']}{'ANALISADOR DE NÚMERO PRIMO':^40}{cores['cls']}")
print(f'{cores["amarelo"]}-={cores["cls"]}' * 20)
n = int(input('Digite um número inteiro: '))
count = 0
for c in range(1, n+1):
    if (n % c == 0):
        count += 1
        print(f'{cores["verde"]}', end='')
    else:
        print(f'{cores["red"]}', end='')
    print(c, end=' ')
print(f'\n{cores["azul"]}{n}{cores["cls"]} foi divisível por {count} números.')
if count > 2:
    print(f'Portanto, ele {cores["red"]}NÃO É UM NÚMERO PRIMO{cores["cls"]}!')
if count == 2:
    print(f'Portanto, ele {cores["verde"]}É UM NÚMERO PRIMO{cores["cls"]}!')
