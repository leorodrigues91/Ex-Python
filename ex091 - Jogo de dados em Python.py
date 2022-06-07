#   Crie um programa onde 4 jogadores joguem um dado e tanham resultados aleatórios.
#   Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem,
#   sabendo que o vencedor tirou o maior número do dado.

#   CABEÇALHO APENAS PARA EFEITOS VISUAIS
cores = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'verde':'\033[1:32m',
         'amarelo': '\033[1:33m',
         'negrito': '\033[1m',
         'cls': '\033[m'}
print(f'{cores["amarelo"]}-={cores["cls"]}' * 25)
print(f"{cores['verde']}{'JOGO DE DADOS EM PYTHON':^50}{cores['cls']}")
print(f'{cores["amarelo"]}-={cores["cls"]}' * 25)

#   INÍCIO DO PROGRAMA

from random import randint
from time import sleep

jogo = {}
ranking = []
print(f'{" >> VALORES SORTEADOS << ":-^50}')
for c in range(1,5):
    jogo['jogador'] = f'jogador{c}'
    jogo['dado'] = randint(1, 6)
    sleep(1)
    print(f'{"O":>5} {jogo["jogador"]} tirou {jogo["dado"]}')
    ranking.append(jogo.copy())
sleep(1)

print(f'{" >> RANKING DOS JOGADORES << ":-^50}')
# ORDENANDO OS DADOS DO DICIONÁRIO NA LISTA, DO MAIOR PARA O MENOR, PELO VALOR RETIRADO NO DADO
ranking.sort(key = lambda dado: dado["dado"], reverse = True)
for c in range(len(ranking)):
    sleep(1)
    print(f'{c + 1:>5}º LUGAR: {ranking[c]["jogador"]} com {ranking[c]["dado"]}')
