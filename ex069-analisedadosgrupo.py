cores = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'verde':'\033[1:32m',
         'amarelo': '\033[1:33m',
         'negrito': '\033[1m',
         'cls': '\033[m'}
print(f'{cores["amarelo"]}-={cores["cls"]}' * 20)
print(f"{cores['verde']}{'ANÁLISE DE DADOS':^40}{cores['cls']}")
print(f'{cores["amarelo"]}-={cores["cls"]}' * 20)
print(f'{"CADASTRE UMA PESSOA":^40}')
print('-' * 40)
masc = maior = fem = total = 0
while True:
    idade = int(input('IDADE: ').strip())
    sexo = ' '
    while sexo not in 'MF' or sexo == '':
        sexo = str(input('SEXO [M/F]: ').strip().upper())
    if idade > 18:
        maior += 1
    if sexo == 'M':
        masc += 1
    if idade < 20 and sexo in 'Ff':
        fem += 1
    print('-' * 40)
    total += 1
    resp = ' '
    while resp not in 'SN' or resp == '':
        resp = str(input('DESEJA CONTINUAR? [S/N] ').strip().upper())
    if resp == 'N':
        break
print('-' * 40)
print(f'FORAM CADASTRADAS {total} PESSOAS.\n'
      f'{maior} DELAS TEM MAIS DE 18 ANOS.')
if masc == 0 or masc > 1:
    print(f'AO TODO TEMOS {masc} HOMENS CADASTRADOS.')
else:
    print(f'AO TODO TEMOS {masc} HOMEM CADASTRADO.')
if fem == 0 or fem > 1:
    print(f'E TEMOS {fem} MULHERES COM MENOS DE 20 ANOS.')
else:
    print(f'E TEMOS {fem} MULHER COM MENOS DE 20 ANOS.')
print('-' * 40)
