cores = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'verde':'\033[1:32m',
         'amarelo': '\033[1:33m',
         'negrito': '\033[1m',
         'cls': '\033[m'}
print(f'{cores["amarelo"]}-={cores["cls"]}' * 25)
print(f"{cores['verde']}{'LISTA DE PREÇOS TUPLA':^50}{cores['cls']}")
print(f'{cores["amarelo"]}-={cores["cls"]}' * 25)
tupla = ('Mouse', 15.00, 'Teclado', 23.50, 'Monitor', 940.00, 'Headphone', 235.40,
          'Joypad', 128.35, 'Mousepad', 57.32)
for pos in range(0, len(tupla)):
    if pos % 2 == 0:
        print(f'{tupla[pos]:.<30}', end='')
    else:
        print(f'R$ {tupla[pos]:>7.2f}')

'''produto = []
preco = []
for prod in range(0, len(tupla), 2):
    produto.append(tupla[prod])
for valor in range(1, len(tupla), 2):
    preco.append(tupla[valor])
pos = -1
while True:
    pos += 1
    if pos == len(produto):
        break
    print(f'{produto[pos]:.<30}{"R$ "}{preco[pos]:>6,.2f}')
print('-' * 50)'''
