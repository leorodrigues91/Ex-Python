#   Crie um programa onde o usuário possa digitar 7 valores numéricos e cadastre-os
#   em uma lista única que mantenha separados os valores pares e ímpares.
#   No final, mostre os valores pares e ímpares em ordem crescente.

#   Cabeçalho apenas para efeitos visuais
cores = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'verde':'\033[1:32m',
         'amarelo': '\033[1:33m',
         'negrito': '\033[1m',
         'cls': '\033[m'}
print(f'{cores["amarelo"]}-={cores["cls"]}' * 25)
print(f"{cores['verde']}{'LISTA COMPOSTA E ANÁLISE DE DADOS':^50}{cores['cls']}")
print(f'{cores["amarelo"]}-={cores["cls"]}' * 25)

#   Início do programa
geral = [[], []]
for n in range(1, 8):
    num = int(input(f'DIGITE O {n}º VALOR: '))
    if num % 2 == 0:
        geral[0].append(num)
    else:
        geral[1].append(num)
geral[0].sort()
geral[1].sort()
print('-' * 50)
print(f'OS VALORES PARES SÃO: {geral[0]}')
print(f'OS VALORES ÍMPARES SÃO: {geral[1]}')
