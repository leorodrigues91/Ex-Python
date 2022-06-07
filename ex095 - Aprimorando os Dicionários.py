#   Aprimorando o EX093 para que funcione com vários jogadores.
#   Incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

#   CABEÇALHO APENAS PARA EFEITOS VISUAIS
cores = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'verde':'\033[1:32m',
         'amarelo': '\033[1:33m',
         'negrito': '\033[1m',
         'cls': '\033[m'}
print(f'{cores["amarelo"]}-={cores["cls"]}' * 35)
print(f"{cores['verde']}{'CADASTRO DE JOGADORES':^70}{cores['cls']}")
print(f'{cores["amarelo"]}-={cores["cls"]}' * 35)

#   INÍCIO DO PROGRAMA

from time import sleep

jogador = {}
equipe = []
gols = []

while True:
    jogador["Nome"] = str(input('Nome: ').strip().upper())
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    if partidas > 0:
        for p in range(partidas):
            gols.append(int(input(f'Quantos gols na partida {p + 1}? ')))
        jogador["Gols"] = gols[:]
        jogador["Total"] = sum(gols)
    equipe.append(jogador.copy())

    while True:
        resp = str(input('Quer continuar [S/N]? ').strip().upper())
        if resp == 'S' or resp == 'N':
            jogador.clear()
            gols.clear()
            break
        print(f'{cores["red"]}OPÇÃO INVÁLIDA! UTILIZE APENAS "S" OU "N".{cores["cls"]}')
    if resp == 'N':
        break
    print('-' * 70)

print('-' * 70)
print(equipe)
print('-' * 70)

print(f'{"COD":<5}{"NOME":<20}{"TOTAL[GOLS]":<15}{"GOLS/PARTIDA":<10}')
for i, j in enumerate(equipe):
    print(f'{i:<5}{j["Nome"]:<20}{j["Total"]:<15}{j["Gols"]}')

while True:
    print('-' * 70)
    print('GOSTARIA DE VER OS DADOS DE QUAL JOGADOR?\n'
          'INFORME O COD DO JOGADOR ("999" FINALIZA)')
    n = int(input('COD: '))
    if n == 999:
        print('FINALIZANDO O PROGRAMA...')
        sleep(0.75)
        break
    if n >= len(equipe):
        print(f'{cores["red"]}NÃO EXISTE JOGADOR COM CÓDIGO {n}! TENTE NOVAMENTE.{cores["cls"]}')
    else:
        print(f' —— LEVANTANDO OS DADOS DO JOGADOR "{equipe[n]["Nome"]}":')
        sleep(0.75)
        for i, j in enumerate(equipe[n]['Gols']):
            print(f'    Na partida {i + 1} fez {j} gol(s)')
            sleep(0.75)

print(f'{f" <<< VOLTE SEMPRE >>> ":-^70}')
