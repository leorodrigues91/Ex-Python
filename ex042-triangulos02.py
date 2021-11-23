cores = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'verde':'\033[1:32m',
         'amarelo': '\033[1:33m',
         'cls': '\033[m'}
print(f'{cores["amarelo"]}-={cores["cls"]}' * 15)
print(f"{cores['azul']}{'ANALISADOR DE TRIÂNGULOS':^30}{cores['cls']}")
print(f'{cores["amarelo"]}-={cores["cls"]}' * 15)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if (a < b + c) and (b < a + c) and (c < a + b):
    print(f'Os segmentos acima {cores["verde"]}PODEM FORMAR{cores["cls"]} um triângulo.')
    if a == b and a == c:
        print(f'Tipo do triângulo: {cores["azul"]}EQUILÁTERO{cores["cls"]}')
    elif (a == b != c) or (a == c != b) or (b == c != a):
        print(f'Tipo do triângulo: {cores["azul"]}ISÓSCELES{cores["cls"]}')
    elif a != b and a != c and b != c:
        print(f'Tipo do triângulo: {cores["azul"]}ESCALENO{cores["cls"]}')
else:
    print(f'Os segmentos acima {cores["red"]}NÃO PODEM{cores["cls"]} formar um triângulo.')
