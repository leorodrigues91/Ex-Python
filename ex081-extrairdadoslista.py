cores = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'verde':'\033[1:32m',
         'amarelo': '\033[1:33m',
         'negrito': '\033[1m',
         'cls': '\033[m'}
print(f'{cores["amarelo"]}-={cores["cls"]}' * 25)
print(f"{cores['verde']}{'EXTRAIR DADOS DE LISTA':^50}{cores['cls']}")
print(f'{cores["amarelo"]}-={cores["cls"]}' * 25)
num = []
while True:
    n = int(input('DIGITE UM VALOR: '))
    num.append(n)
    resp = str(input('QUER CONTINUAR? [S/N] ').strip().upper())
    if resp in 'Nn':
        break
print('-' * 50)
print(f'FORAM DIGITADOS {len(num)} VALORES.')
num.sort(reverse=True)
print(f'OS VALORES EM ORDEM DECRESCENTE SÃO:\n{num}')
if 5 in num:
    print(f'O NÚMERO 5 ESTÁ NA POSIÇÃO {num.index(5)} DA LISTA.')
else:
    print('O NÚMERO 5 NÃO FOI ENCONTRADO NA LISTA.')
