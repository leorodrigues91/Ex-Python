from datetime import date
cores = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'verde':'\033[1:32m',
         'amarelo': '\033[1:33m',
         'cls': '\033[m'}
print(f'{cores["amarelo"]}-={cores["cls"]}' * 15)
print(f"{cores['verde']}{'ALISTAMENTO MILITAR':^30}{cores['cls']}")
print(f'{cores["amarelo"]}-={cores["cls"]}' * 15)
ano = int(input('Informe o seu ano de nascimento: '))
idade = date.today().year - ano
if idade > 18:
    print(f'Já se passaram {cores["azul"]}{idade - 18}{cores["cls"]} anos do seu alistamento obrigatório.')
elif idade == 18:
    print(f'Já chegou o momento de realizar o seu alistamento obrigatório.')
elif idade < 18:
    print(f'Restam {cores["azul"]}{18 - idade}{cores["cls"]} anos até o seu alistamento obrigatório.')
