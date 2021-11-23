cores = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'verde':'\033[1:32m',
         'amarelo': '\033[1:33m',
         'negrito': '\033[1m',
         'cls': '\033[m'}
print(f'{cores["amarelo"]}-={cores["cls"]}' * 25)
print(f"{cores['verde']}{'TUPLA ANÁLISE DE VALORES':^50}{cores['cls']}")
print(f'{cores["amarelo"]}-={cores["cls"]}' * 25)
num = []
cont = 0
n1 = int(input('DIGITE UM NÚMERO: '))
n2 = int(input('DIGITE OUTRO NÚMERO: '))
n3 = int(input('DIGITE MAIS UM NÚMERO: '))
n4 = int(input('DIGITE O ÚLTIMO NÚMERO: '))
num.extend((n1, n2, n3, n4))
tupla = num
for nove in tupla:
    nove = tupla.count(9)
print(f'O VALOR 9 APARECEU {nove} VEZES.')
try:
    tres = tupla.index(3)
except:
    tres = 0
if tres == 0:
    print('O VALOR 3 NÃO FOI DIGITADO EM NENHUMA POSIÇÃO.')
else:
    print(f'O VALOR 3 APARECEU NA {tres + 1}ª POSIÇÃO.')
par = []
for p in range(0, len(num)):
    if num[p] % 2 == 0:
       par.append(num[p])
print(f'ENTRE OS VALORES DIGITADOS, ESTES SÃO PARES: {", ".join(map(str, par))}')
#print(num)
#print(f'Essa é a tupla: {tupla}')