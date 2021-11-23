cores = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'verde':'\033[1:32m',
         'amarelo': '\033[1:33m',
         'negrito': '\033[1m',
         'cls': '\033[m'}
print(f'{cores["amarelo"]}-={cores["cls"]}' * 20)
print(f"{cores['verde']}{'LOJA TESTE':^40}{cores['cls']}")
print(f'{cores["amarelo"]}-={cores["cls"]}' * 20)
resp = 'S'
gasto = total = mais = 0
prod = resp = ''
barato = []
while True:
    while prod == '':
        prod = str(input('NOME DO PRODUTO: ').strip().upper())
    preco = float(input('PREÇO: R$ ').strip())
    print('-' * 40)
    total += 1
    gasto += preco
    barato.extend((prod, preco))
    if preco < barato[1]:
        barato.insert(0, prod)
        barato.insert(1, preco)
    if preco > 1000:
        mais += 1
    while resp not in 'SN' or resp == '':
        resp = str(input('DESEJA CONTINUAR? [S/N] ').strip().upper())
    if resp == 'N':
        break
    print('-' * 40)
print(f'{"---------- COMPRA FINALIZADA ----------":^40}')
print(f'AO TODO FORAM COMPRADOS {total} PRODUTOS.')
print(f'O TOTAL GASTO É: R$ {gasto:.2f}')
if mais == 0 or mais > 1:
    print(f'TEMOS {mais} PRODUTOS CUSTANDO MAIS DE R$ 1000.')
else:
    print(f'TEMOS {mais} PRODUTO CUSTANDO MAIS DE R$ 1000.')
print(f'O PRODUTO MAIS BARATO FOI {barato[0]} CUSTANDO R$ {barato[1]:.2f}')
