#   Faça um programa que tenha uma lista chamada "números" e duas funções
#   chamadas "sorteia()" e "somaPar()". A primeira função vai sortear 5 números
#   e vai colocá-los dentro da lista. A segunda função vai mostrar a soma entre todos
#   os valores pares sorteador pela função anterior.

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
título('SORTEAR E SOMAR - FUNÇÃO')

#   INÍCIO DO PROGRAMA

from random import randint
from time import sleep

numeros = []
def sorteia(lst):
    for c in range(0, 5):
        lst.append(randint(1, 10))
    print('Sorteando 5 valores da lista: ', end='')
    sleep(0.5)
    for i, v in enumerate(lst):
        print(f'{v}', end=' ')
        sleep(0.5)
    print('PRONTO!')

def somaPar(lst):
    soma = 0
    for i, v in enumerate(lst):
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores pares de {lst}, temos: {soma}')


sorteia(numeros)
somaPar(numeros)
