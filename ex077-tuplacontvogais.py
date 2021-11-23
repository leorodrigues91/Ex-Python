cores = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'verde':'\033[1:32m',
         'amarelo': '\033[1:33m',
         'negrito': '\033[1m',
         'cls': '\033[m'}
print(f'{cores["amarelo"]}-={cores["cls"]}' * 25)
print(f"{cores['verde']}{'CONTANDO VOGAIS TUPLA':^50}{cores['cls']}")
print(f'{cores["amarelo"]}-={cores["cls"]}' * 25)
tupla = ('arroz', 'feijao', 'açucar', 'sal', 'batata',
         'legumes', 'banana', 'suco')
for itens in tupla:
    print(f'Na palavra {itens.upper()} temos ', end='')
    for letra in itens:
        if letra in 'aeiou':
            print(f'{letra}', end=' ')
    print('\n')

'''for itens in tupla:
    vogal = []
    print(f'Na palavra {itens.upper()} temos:', end=' ')
    for letra in itens:
        if letra in 'aeiou':
            vogal.append(letra)
    print(f'{" ".join(map(str, vogal))}')'''