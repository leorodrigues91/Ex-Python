from datetime import date
cores = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'verde':'\033[1:32m',
         'amarelo': '\033[1:33m',
         'cls': '\033[m'}
print(f'{cores["amarelo"]}-={cores["cls"]}' * 15)
print(f"{cores['azul']}{'CATEGORIAS NATAÇÃO POR IDADE':^30}{cores['cls']}")
print(f'{cores["amarelo"]}-={cores["cls"]}' * 15)
ano = date.today().year
nascimento = int(input('Ano de nacimento do(a) atleta: '))
idade = ano - nascimento
print(f'O(a) atleta tem {cores["azul"]}{idade}{cores["cls"]} anos.')
if idade <= 9:
    print(f'Categoria: {cores["verde"]}MIRIM{cores["cls"]}.')
elif idade <= 14:
    print(f'Categoria: {cores["verde"]}INFANTIL{cores["cls"]}.')
elif idade <= 17:
    print(f'Categoria: {cores["verde"]}JUNIOR{cores["cls"]}.')
elif idade <= 28:
    print(f'Categoria: {cores["verde"]}SÊNIOR{cores["cls"]}.')
elif idade > 28:
    print(f'Categoria: {cores["verde"]}MASTER{cores["cls"]}.')
