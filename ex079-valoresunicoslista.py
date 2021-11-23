cores = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'verde':'\033[1:32m',
         'amarelo': '\033[1:33m',
         'negrito': '\033[1m',
         'cls': '\033[m'}
print(f'{cores["amarelo"]}-={cores["cls"]}' * 25)
print(f"{cores['verde']}{'VALORES ÚNICOS EM LISTA':^50}{cores['cls']}")
print(f'{cores["amarelo"]}-={cores["cls"]}' * 25)
valor = []
while True:
    n = int(input('DIGITE UM VALOR: '))
    if n not in valor:
        valor.append(n)
        print(f'{cores["verde"]}VALOR ADICIONADO COM SUCESSO!{cores["cls"]}')
    else:
        print(f'{cores["red"]}VALOR JÁ EXISTENTE! NÃO SERÁ ADICIONADO...{cores["cls"]}')
    resp = str(input('DESEJA CONTINUAR? [S/N] ').upper().strip())
    if resp == 'N':
        break
    print('-' * 50)
valor.sort()
print(f'VOCÊ DIGITOU OS VALORES: {valor}')
