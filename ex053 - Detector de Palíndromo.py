cores = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'verde':'\033[1:32m',
         'amarelo': '\033[1:33m',
         'negrito': '\033[1m',
         'cls': '\033[m'}
print(f'{cores["amarelo"]}-={cores["cls"]}' * 15)
print(f"{cores['verde']}{'ANALISADOR DE PALINDROMOS':^30}{cores['cls']}")
print(f'{cores["amarelo"]}-={cores["cls"]}' * 15)
frase = str(input('Inisira uma frase para análise: ')).strip().replace(' ', '').upper()
inverso = frase[::-1].upper()
print(f'O inverso de {cores["azul"]}{frase}{cores["cls"]} é {cores["azul"]}{inverso}{cores["cls"]}.')
print('-' * 30)
if inverso == frase:
    print(f'{cores["verde"]}A frase é um palídromo!{cores["cls"]}')
else:
    print(f'{cores["red"]}A frase não é um palíndromo!{cores["cls"]}')
print('-' * 30)
