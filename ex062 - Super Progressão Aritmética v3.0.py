cores = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'verde':'\033[1:32m',
         'amarelo': '\033[1:33m',
         'negrito': '\033[1m',
         'cls': '\033[m'}
print(f'{cores["amarelo"]}-={cores["cls"]}' * 15)
print(f"{cores['verde']}{'PROGRESSÃO ARITMÉTICA':^30}{cores['cls']}")
print(f'{cores["amarelo"]}-={cores["cls"]}' * 15)
a1 = int(input('Primeiro termo da PA: '))
r = int(input('Razão da PA: '))
pa = a1
count = 1
total = 0
n = 10
while n != 0:
    total += n
    while count <= total:
        print(pa, end=' -> ')
        pa += r
        count += 1
    print('PAUSA')
    n = int(input('Quantos termos você gostaria de mostrar a mais? '))
print('-' * 40)
print(f'PROGRESSÃO FINALIZADA COM {cores["azul"]}{total}{cores["cls"]} TERMOS MOSTRADOS.')
