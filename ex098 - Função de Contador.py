#   Faça um programa que tenha uma função chamada "contador()",
#   que receba 3 parâmetros: 'início, fim e passo' e realize a contagem.
#   Seu programa tem que realizar três contagens através da função criada:
#   A) De 1 até 10, de 1 em 1;
#   B) De 10 até 0, de 2 em 2;
#   C) Uma contagem personalizada.

#   FUNÇÕES UTILIZADAS NA ESTÉTICA DO PROGRAMA
cores = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'verde':'\033[1:32m',
         'amarelo': '\033[1:33m',
         'negrito': '\033[1m',
         'cls': '\033[m'}
def título(txt):
    print(f'{cores["amarelo"]}-={cores["cls"]}' * 25)
    print(f"{cores['verde']}{txt:^50}{cores['cls']}")
    print(f'{cores["amarelo"]}-={cores["cls"]}' * 25)

#   CABEÇALHO APENAS PARA EFEITOS VISUAIS
título('FUNÇÃO CONTADOR')

#   INÍCIO DO PROGRAMA

from time import sleep
def contador(i, f, p):
    if p == 0:
        p = 1
    elif p < 0:
        p *= -1
    print(f'Contagem de {i} até {f}, de {p} em {p}:')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.3)
            cont += p
        sleep(0.3)
        print('FIM!')
        sleep(0.3)
        print('-' * 30)
        sleep(0.5)
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.3)
            cont -= p
        sleep(0.3)
        print('FIM!')
        sleep(0.3)
        print('-' * 30)
        sleep(0.5)


contador(1, 10, 1)
contador(10, 0, 2)
print('AGORA É SUA VEZ DE PERSONALIZAR A CONTAGEM!')
ini = int(input('INÍCIO: '))
fim = int(input('FINAL: '))
pas = int(input('PASSO: '))
contador(ini, fim, pas)
