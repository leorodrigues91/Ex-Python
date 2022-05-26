cores = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'amarelo': '\033[1:33m',
         'cls': '\033[m'}
print(f'{cores["amarelo"]}-={cores["cls"]}' * 15)
print(f"{cores['azul']}{'CONVERSOR DE BASE NUMÉRICA':^30}{cores['cls']}")
print(f'{cores["amarelo"]}-={cores["cls"]}' * 15)
num = int(input('Informe um número inteiro para conversão: '))
print('Ok. Agora escolha uma das bases numéricas abaixo:')
print(f'[ {cores["azul"]}1{cores["cls"]} ] para {cores["red"]}binário{cores["cls"]};\n'
      f'[ {cores["azul"]}2{cores["cls"]} ] para {cores["red"]}octal{cores["cls"]};\n'
      f'[ {cores["azul"]}3{cores["cls"]} ] para {cores["red"]}hexadecimal{cores["cls"]};')
base = int(input('Digite aqui sua escolha: '))
if base == 1:
    print(f'O número {cores["azul"]}{num}{cores["cls"]} em {cores["red"]}binário{cores["cls"]} é: \033[1m{format(num, "b")}\033[m')
elif base == 2:
    print(f'O número {cores["azul"]}{num}{cores["cls"]} em {cores["red"]}octal{cores["cls"]} é: \033[1m{format(num, "o")}\033[m')
elif base == 3:
    print(f'O número {cores["azul"]}{num}{cores["cls"]} em {cores["red"]}hexadecimal{cores["cls"]} é: \033[1m{format(num, "x")}\033[m')
