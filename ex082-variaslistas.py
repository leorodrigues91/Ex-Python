cores = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'verde':'\033[1:32m',
         'amarelo': '\033[1:33m',
         'negrito': '\033[1m',
         'cls': '\033[m'}
print(f'{cores["amarelo"]}-={cores["cls"]}' * 25)
print(f"{cores['verde']}{'DIVIDIR VALORES EM LISTAS':^50}{cores['cls']}")
print(f'{cores["amarelo"]}-={cores["cls"]}' * 25)
lista = []
par = []
impar = []
while True:
    n = int(input('DIGITE UM NÚMERO: '))
    lista.append(n)
    resp = str(input('QUER CONTINUAR? [S/N] ').strip().upper())
    if resp in 'Nn':
        break
for c in range(len(lista)):
    if lista[c] % 2 == 0:
        par.append(lista[c])
    else:
        impar.append(lista[c])
print('-' * 50)
print(f'A LISTA COMPLETA É: {lista}')
print(f'A LISTA DE PARES É: {par}')
print(f'A LISTA DE IMPARES É: {impar}')
