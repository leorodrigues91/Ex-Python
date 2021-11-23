cores = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'verde':'\033[1:32m',
         'amarelo': '\033[1:33m',
         'negrito': '\033[1m',
         'cls': '\033[m'}
print(f'{cores["amarelo"]}-={cores["cls"]}' * 20)
print(f"{cores['verde']}{'MÉDIA DOS VALORES':^40}{cores['cls']}")
print(f'{cores["amarelo"]}-={cores["cls"]}' * 20)
r = 's'
count = 0
num = []
while r == 's':
    n = int(input('Digite um valor: '))
    num.append(n)
    count += 1
    r = str(input('Quer continuar?? [S/N] ').lower())
soma = sum(num)
media = soma / count
num = sorted(num)
print('-' * 40)
print(f'VOCÊ DIGITOU {cores["azul"]}{count}{cores["cls"]} VALORES.')
print(f'A MÉDIA ENTRE ESSES VALORES É: {cores["azul"]}{media:.2f}{cores["cls"]}')
print(f'O MAIOR VALOR DIGITADO FOI: {cores["azul"]}{num[-1]}{cores["cls"]}\n'
      f'O MENOR VALOR DIGITADO FOI: {cores["azul"]}{num[0]}{cores["cls"]}')
print('-' * 40)
