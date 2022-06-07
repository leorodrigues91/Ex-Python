#   Faça um programa que leia nome e média de um aluno, guardando também a situação
#   em um dicionário. No final, mostre o conteúdo da estrutura na tela.

#   CABEÇALHO APENAS PARA EFEITOS VISUAIS
cores = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'verde':'\033[1:32m',
         'amarelo': '\033[1:33m',
         'negrito': '\033[1m',
         'cls': '\033[m'}
print(f'{cores["amarelo"]}-={cores["cls"]}' * 25)
print(f"{cores['verde']}{'ANÁLISE DE MÉDIA':^50}{cores['cls']}")
print(f'{cores["amarelo"]}-={cores["cls"]}' * 25)

#   INÍCIO DO PROGRAMA

alunos = {}

alunos['Nome'] = str(input('NOME: ').strip().upper())
alunos['Média'] = float(input(f'MÉDIA DE {alunos["Nome"]}: '))

if alunos['Média'] >= 7:
    alunos['Situação'] = 'APROVADO(A)!!'
elif 5 > alunos['Média']:
    alunos['Situação'] = 'REPROVADO(A)!!'
else:
    alunos['Situação'] = 'EM RECUPERAÇÃO!!'

print('-' * 50)

for k, v in alunos.items():
    print(f'{k:.<15} {v}')
