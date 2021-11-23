cores = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'verde':'\033[1:32m',
         'amarelo': '\033[1:33m',
         'negrito': '\033[1m',
         'cls': '\033[m'}
print(f'{cores["amarelo"]}-={cores["cls"]}' * 20)
print(f"{cores['verde']}{'TRATANDO VALORES':^40}{cores['cls']}")
print(f'{cores["amarelo"]}-={cores["cls"]}' * 20)
print('DIGITE QUANTOS VALORES DESEJAR.')
print('-' * 40)
soma = 0
n = 0
count = 0
while True:
    n = int(input('DIGITE UM VALOR [999 para finalizar]: '))
    if n == 999:
        break
    soma += n
    count += 1
print(f'A soma dos {count} valores é igual a: {cores["azul"]}{soma}{cores["cls"]}')
