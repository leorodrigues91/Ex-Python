#   Faça um programa que tenha uma função chamada "área()", que receba as dimensões
#   de um terrerno retangular (largura e comprimento) e mostre a área do terreno.


#   FUNÇÕES UTILIZADAS NA ESTÉTICA DO PROGRAMA
cores = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'verde':'\033[1:32m',
         'amarelo': '\033[1:33m',
         'negrito': '\033[1m',
         'cls': '\033[m'}
def título(txt):
    print(f'{cores["amarelo"]}-={cores["cls"]}' * 35)
    print(f"{cores['verde']}{txt:^70}{cores['cls']}")
    print(f'{cores["amarelo"]}-={cores["cls"]}' * 35)

#   CABEÇALHO APENAS PARA EFEITOS VISUAIS
título('CALCULANDO ÁREA DE TERRENOS')

#   INÍCIO DO PROGRAMA
def area(l, c):
    a = l * c
    print(f'A área de um terreno {l} x {c} é de: {a} m²')


larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
area(larg, comp)
