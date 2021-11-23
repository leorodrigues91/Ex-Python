cores = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'verde':'\033[1:32m',
         'amarelo': '\033[1:33m',
         'negrito': '\033[1m',
         'cls': '\033[m'}
print(f'{cores["amarelo"]}-={cores["cls"]}' * 15)
print(f"{cores['azul']}{'ANALISADOR DE PESSOAS':^30}{cores['cls']}")
print(f'{cores["amarelo"]}-={cores["cls"]}' * 15)
p1 = []
p2 = []
p3 = []
p4 = []
somaid = []
n = 1
f = 0
for c in range(0, 4):
    print(f'----- {n}ª PESSOA -----')
    nome = str(input(f'Nome: ').upper().strip())
    idade = int(input(f'Idade: '))
    sexo = str(input(f'Sexo [M/F]: ').upper().strip())
    if n == 1:
        p1.extend((nome, idade, sexo))
        somaid.append(idade)
        if p1[2] == 'M':
            velho = p1
        n += 1
    elif n == 2:
        p2.extend((nome, idade, sexo))
        somaid.append(idade)
        n += 1
        if p2[2] == 'M' and p2[1] > velho[1]:
            velho = p2
    elif n == 3:
        p3.extend((nome, idade, sexo))
        somaid.append(idade)
        n += 1
        if p3[2] == 'M' and p3[1] > velho[1]:
            velho = p3
    elif n == 4:
        p4.extend((nome, idade, sexo))
        somaid.append(idade)
        n += 1
        if p4[2] == 'M' and p4[1] > velho[1]:
            velho = p4
    if sexo == 'F' and idade < 20:
        f += 1
print('-' * 40)
media = sum(somaid) / 4
print(f'A média de idade entre essas pessoas é: {cores["azul"]}{media:.1f}{cores["cls"]} anos.')
print(f'O homem mais velho tem {cores["azul"]}{velho[1]}{cores["cls"]} anos e se chama {cores["azul"]}{velho[0]}{cores["cls"]}.')
print(f'Existem {cores["azul"]}{f}{cores["cls"]} mulheres com menos de 20 anos.')
