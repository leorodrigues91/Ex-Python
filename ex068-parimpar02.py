from random import randint
cores = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'verde':'\033[1:32m',
         'amarelo': '\033[1:33m',
         'negrito': '\033[1m',
         'cls': '\033[m'}
print(f'{cores["amarelo"]}-={cores["cls"]}' * 20)
print(f"{cores['verde']}{'JOGO PAR OU IMPAR':^40}{cores['cls']}")
print(f'{cores["amarelo"]}-={cores["cls"]}' * 20)
pc = randint(0, 11)
count = 0
while True:
    jogador = int(input('DIGITE UM VALOR PARA COMEÇAR: '))
    par_impar = str(input('PAR OU ÍMPAR? ex:[P/I] ').strip().upper())
    while par_impar not in 'PI' or par_impar == '':
        par_impar = str(input('PAR OU ÍMPAR? ex:[P/I] ').strip().upper())
    print('-' * 40)
    soma = jogador + pc
    if soma % 2 == 0:
        print(f'VOCÊ JOGOU {cores["azul"]}{jogador}{cores["cls"]} E O COMPUTADOR {cores["azul"]}{pc}{cores["cls"]}.\n'
              f'TOTAL = {cores["azul"]}{soma}{cores["cls"]}. DEU PAR!')
        print('-' * 40)
        if par_impar == 'P':
            print(f'{cores["verde"]}PARABÉNS, VOCÊ VENCEU!!{cores["cls"]}')
            print('VAMOS JOGAR NOVAMENTE...')
            print('-' * 40)
            count += 1
        else:
            print(f'{cores["red"]}QUE PENA, VOCÊ PERDEU!{cores["cls"]}')
            break
    else:
        print(f'VOCÊ JOGOU {cores["azul"]}{jogador}{cores["cls"]} E O COMPUTADOR {cores["azul"]}{pc}{cores["cls"]}.\n'
              f'TOTAL = {cores["azul"]}{soma}{cores["cls"]}. DEU IMPAR!')
        print('-' * 40)
        if par_impar == 'I':
            print(f'{cores["verde"]}PARABÉNS, VOCÊ VENCEU!!{cores["cls"]}')
            print('VAMOS JOGAR NOVAMENTE...')
            print('-' * 40)
            count +=1
        else:
            print(f'{cores["red"]}QUE PENA, VOCÊ PERDEU!{cores["cls"]}')
            break
print('-' * 40)
print(f'GAME OVER!! VOCÊ CONSEGUIU VENCER {count} VEZES.')
