cores = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'verde':'\033[1:32m',
         'amarelo': '\033[1:33m',
         'negrito': '\033[1m',
         'cls': '\033[m'}
print(f'{cores["amarelo"]}-={cores["cls"]}' * 15)
print(f"{cores['verde']}{'ANALISADOR DE PESO':^30}{cores['cls']}")
print(f'{cores["amarelo"]}-={cores["cls"]}' * 15)
n = 1
pesos = []
for c in range(0,5):
    p = float(input(f'Informe o {n}º peso: '))
    n += 1
    pesos.append(p)
pesos = sorted(pesos)
maior = pesos[-1]
menor = pesos[0]
#print(pesos)
print('-=' *20)
print(f'O maior peso é: {cores["azul"]}{maior}{cores["cls"]} Kg\n'
      f'O menor peso é: {cores["azul"]}{menor}{cores["cls"]} Kg')
print('-=' *20)
