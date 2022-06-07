#   Faça um programa que tenha uma função chamada "maior()",
#   que receba vários parâmetros com valores inteiros.
#   Seu programa tem que analisar todos os valores e dizer qual deles é maior.

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
título('DESCOBRIR MAIOR NÚMERO - FUNÇÃO')

#   INÍCIO DO PROGRAMA

from time import sleep
def maior(* num):
    mai = 0
    print('Analisando os valores informados...')
    sleep(0.3)
    for v in num:
        if v >= mai:
            mai = v
        print(f'{v}', end=' ')
        sleep(0.3)
    print(f'Foram informados {len(num)} valores.')
    print(f'O maior valor informado foi {mai}.')
    print('-' * 50)

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

