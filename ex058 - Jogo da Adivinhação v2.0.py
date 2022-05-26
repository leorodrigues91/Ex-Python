cores = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'verde':'\033[1:32m',
         'amarelo': '\033[1:33m',
         'negrito': '\033[1m',
         'cls': '\033[m'}
print(f'{cores["amarelo"]}-={cores["cls"]}' * 20)
print(f"{cores['azul']}{'ADIVINHE O NÚMERO':^40}{cores['cls']}")
print(f'{cores["amarelo"]}-={cores["cls"]}' * 20)
from random import randint
from time import sleep
num = -1
count = 0
print(f'PENSAREI EM UM NÚMERO ENTRE {cores["azul"]}0{cores["cls"]} E {cores["azul"]}10{cores["cls"]}...')
n = randint(0, 10)
sleep(1.5)
print('OK. AGORA TENTE ADIVINHAR O NÚMERO!')
sleep(1)
while num != n:
    num = int(input('DIGITE SUA ESCOLHA: '))
    count += 1
    if num > n:
        print(f'{cores["red"]}MENOS... TENTE OUTRA VEZ!{cores["cls"]}')
    elif num < n:
        print(f'{cores["red"]}MAIS... TENTE OUTRA VEZ!{cores["cls"]}')
print(f'{cores["verde"]}PARABÉNS!{cores["cls"]}\n'
      f'O NÚMERO QUE PENSEI FOI {cores["azul"]}{n}{cores["cls"]}.\n'
      f'VOCÊ LEVOU {cores["azul"]}{count}{cores["cls"]} TENTATIVAS PARA ACERTAR.')
