cores = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'verde':'\033[1:32m',
         'amarelo': '\033[1:33m',
         'negrito': '\033[1m',
         'cls': '\033[m'}
print(f'{cores["amarelo"]}-={cores["cls"]}' * 20)
print(f"{cores['verde']}{'TRATANDO VALORES':^40}{cores['cls']}")
print(f'{cores["amarelo"]}-={cores["cls"]}' * 20)
print('DIGITE QUANTOS VALORES DESEJAR.\n'
      f'E DIGITE {cores["azul"]}"999"{cores["cls"]} PARA FINALIZAR.')
print('-' * 40)
soma = 0
n = 0
count = 0
n = int(input('DIGITE UM VALOR: '))
while n != 999:
    soma += n
    count += 1
    n = int(input('DIGITE UM VALOR: '))
print(f'Você digitou {cores["azul"]}{count}{cores["cls"]} valores.')
print(f'A soma desses valores é igual a: {cores["azul"]}{soma}{cores["cls"]}')
