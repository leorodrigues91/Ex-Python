cores = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'verde':'\033[1:32m',
         'amarelo': '\033[1:33m',
         'negrito': '\033[1m',
         'cls': '\033[m'}
print(f'{cores["amarelo"]}-={cores["cls"]}' * 20)
print(f"{cores['verde']}{'TABUADAS':^40}{cores['cls']}")
print(f'{cores["amarelo"]}-={cores["cls"]}' * 20)
while True:
    tab = 1
    n = int(input('INFORME UM VALOR PARA VER SUA TABUADA: '))
    if n < 0:
        break
    print('-' * 40)
    while tab <= 10:
        mult = n * tab
        print(f'{n:>12} x {tab:>2} = {mult:>4}')
        tab += 1
    print('-' * 40)
print('PROGRAMA FINALIZADO COM SUCESSO!')
