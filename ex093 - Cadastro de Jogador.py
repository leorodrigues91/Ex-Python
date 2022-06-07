#   Crie um programa que gerencie o aproveitamento de um jogador de futebol.
#   O programa vai ler o nome e quantas partidas ele jogou.
#   Depois vai ler a quantidade de gols feitos em cada uma das partidas.
#   Tudo isso será guardado em um dicionário, incluindo o total de gols feitos.

#   CABEÇALHO APENAS PARA EFEITOS VISUAIS
cores = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'verde':'\033[1:32m',
         'amarelo': '\033[1:33m',
         'negrito': '\033[1m',
         'cls': '\033[m'}
print(f'{cores["amarelo"]}-={cores["cls"]}' * 25)
print(f"{cores['verde']}{'CADASTRO DE JOGADOR':^50}{cores['cls']}")
print(f'{cores["amarelo"]}-={cores["cls"]}' * 25)

#   INÍCIO DO PROGRAMA

jogador = {}
gols = []

jogador["Nome"] = str(input('Nome: ').strip().upper())
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? ').strip())
if partidas > 0:
    for p in range(partidas):
        gols.append(int(input(f'Quantos gols na partida {p + 1}? ').strip()))
    jogador["Gols"] = gols[:]
    jogador["Total"] = sum(gols)

media = jogador["Total"] / partidas

print('-' * 50)
for k, v in jogador.items():
    print(f'{k:.<10}: {v}')
    print()

print('-=' * 25)
print(f'O jogador {jogador["Nome"]} jogou um total de {partidas} partidas.')
for p in range(partidas):
    print(f'{"=>":>6} Na partida {p + 1}, fez {jogador["Gols"][p]} gols.')
print(f'Foi um total de {jogador["Total"]} gols.')
print(f'Uma média de {media} gols/partida.')
