#   Crie um programa que leia nome e duas notas de vários alunos
#   e guarde tudo em uma lista composta. No final, mostre um boletim contendo
#   a média de cada um e permita que o usuário possa mostrar as notas de cada
#   aluno individualmente.

#   CABEÇALHO APENAS PARA EFEITOS VISUAIS
cores = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'verde':'\033[1:32m',
         'amarelo': '\033[1:33m',
         'negrito': '\033[1m',
         'cls': '\033[m'}
print(f'{cores["amarelo"]}-={cores["cls"]}' * 25)
print(f"{cores['verde']}{'MATRIZ EM PYTHON - APRIMORADO':^50}{cores['cls']}")
print(f'{cores["amarelo"]}-={cores["cls"]}' * 25)

#   INÍCIO DO PROGRAMA
from time import sleep

boletim = []
while True:
    alunos = []
    alunos.append(str(input('NOME: ')).strip().capitalize())
    alunos.append(float(input('NOTA 1: ')))
    alunos.append(float(input('NOTA 2: ')))
    boletim.append(alunos[:])
    alunos.clear()
    resp = str(input('QUER CONTINUAR? [S/N] ').strip().upper())
    if resp in 'Nn':
        sleep(0.3)
        break
print('-=' * 25)
print(f'{"No.":<4} {"NOME":<15} {"MÉDIA"}')
print('-' * 30)
for p in boletim:
    media = (p[1] + p[2]) / 2
    print(f'{boletim.index(p):<4} {p[0]:<15} {media:.1f}')
while True:
    print('-' * 50)
    print('GOSTARIA DE VER AS NOTAS DE QUAL ALUNO(A)?\n'
          'INFORME O NÚMERO DO ALUNO ABAIXO. ("999" FINALIZA)')
    n = int(input('No.: '))
    if n == 999:
        print('FINALIZANDO O PROGRAMA...')
        sleep(0.75)
        break
    print(f'AS NOTAS DE {boletim[n][0]} SÃO: {boletim[n][1:]}')
print(f'{f" <<< VOLTE SEMPRE >>> ":-^50}')
