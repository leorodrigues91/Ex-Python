from time import sleep
cores = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'verde':'\033[1:32m',
         'amarelo': '\033[1:33m',
         'negrito': '\033[1m',
         'cls': '\033[m'}
print(f'{cores["amarelo"]}-={cores["cls"]}' * 25)
print(f"{cores['verde']}{'BRASILEIRÃO SÉRIE A 2021':^50}{cores['cls']}")
print(f'{cores["amarelo"]}-={cores["cls"]}' * 25)
times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Bragantino', 'Corinthians', 'Fortaleza', 'Internacional', 'Fluminense',
         'América-MG', 'Ceará', 'Athletico-PR', 'Santos', 'Cuiabá', 'Atlético-GO', 'São Paulo', 'Bahia', 'Juventude',
         'Sport', 'Grêmio', 'Chapecoense')
while True:
    print('ESCOLHA UMA DAS OPÇÕES ABAIXO:\n'
          '[ 1 ] EXIBIR TABELA COMPLETA COM AS POSIÇÕES\n'
          '[ 2 ] EXIBIR OS 5 PRIMEIROS COLOCADOS\n'
          '[ 3 ] EXIBIR OS ÚLTIMOS 4 COLOCADOS\n'
          '[ 4 ] EXIBIR OS TIMES EM ORDEM ALFABÉTICA\n'
          '[ 5 ] ESCOLHA UM TIME PARA SABER SUA POSIÇÃO\n'
          '[ 0 ] FINALIZAR PROGRAMA')
    user = int(input('DIGITE SUA ESCOLHA: '))
    print('-' * 50)
    if user == 0:
        print('FINALIZANDO PROGRAMA...')
        sleep(0.75)
        break
    elif user == 1: # Tabela completa
        for pos, time in enumerate(times):
            print(f'{pos + 1:>2} - {time}')
        print('-' * 50)
    elif user == 2: # 5 primeiros colocados
        print('OS 5 PRIMEIROS COLOCADOS SÃO:')
        for pos, time in enumerate(times[0:5]):
            print(f'{pos + 1:>2} - {time}')
        print('-' * 50)
    elif user == 3: # 4 últimos colocados
        print('OS 4 ÚLTIMOS COLOCADOS SÃO:')
        for time in times[-4:]:
            print(f'- {time}')
        print('-' * 50)
    elif user == 4: # Times em ordem alfabética
        print('\n'.join(map(str, sorted(times))))
        print('-' * 50)
    elif user == 5: # Saber posição de time específico
        time = str(input('INFORME UM TIME PARA SABER SUA COLOCAÇÃO: ').strip().capitalize())
        print(f'{time.upper()} ESTÁ NA {times.index(time) + 1}ª POSIÇÃO.')
        print('-' * 50)
print('-=' * 20)
print('PROGRAMA FINALIZADO COM SUCESSO')