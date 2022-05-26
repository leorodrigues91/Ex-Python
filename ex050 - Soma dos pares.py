cores = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'verde':'\033[1:32m',
         'amarelo': '\033[1:33m',
         'negrito': '\033[1m',
         'cls': '\033[m'}
print(f'{cores["amarelo"]}-={cores["cls"]}' * 15)
print(f"{cores['verde']}{'SOMA DE NÚMEROS PARES':^30}{cores['cls']}")
print(f'{cores["amarelo"]}-={cores["cls"]}' * 15)
soma = 0
for c in range (1, 7):
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        soma += n
print(f'A soma dos valores pares é: {cores["azul"]}{soma}{cores["cls"]}')
