from datetime import date
cores = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'verde':'\033[1:32m',
         'amarelo': '\033[1:33m',
         'negrito': '\033[1m',
         'cls': '\033[m'}
print(f'{cores["amarelo"]}-={cores["cls"]}' * 15)
print(f"{cores['verde']}{'ANALISE DE IDADE':^30}{cores['cls']}")
print(f'{cores["amarelo"]}-={cores["cls"]}' * 15)
n = 1
maior = 0
menor = 0
for c in range(0, 7):
    ano = int(input(f'Informe o {n}º ano de nascimento: '))
    n += 1
    if (date.today().year - ano) >= 18:
        maior += 1
    else:
        menor += 1
print(f'Segundo as informações inseridas, existem:\n'
      f'{cores["azul"]}{maior}{cores["cls"]} pessoas maiores de idade\n'
      f'{cores["azul"]}{menor}{cores["cls"]} pessoas menores de idade')
