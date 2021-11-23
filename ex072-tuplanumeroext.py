cores = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'verde':'\033[1:32m',
         'amarelo': '\033[1:33m',
         'negrito': '\033[1m',
         'cls': '\033[m'}
print(f'{cores["amarelo"]}-={cores["cls"]}' * 20)
print(f"{cores['verde']}{'NÚMERO POR EXTENSO':^40}{cores['cls']}")
print(f'{cores["amarelo"]}-={cores["cls"]}' * 20)
numext = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito',
          'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
          'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('DIGITE UM NÚMERO DE 0 A 20: '))
    if 0 <= num <= 20:
        break
    print(f'{cores["red"]}NÚMERO FORA DA PROPOSTA. TENTE NOVAMENTE.{cores["cls"]}')
print(f'{cores["verde"]}Você digitou o número {numext[num]}.{cores["cls"]}')
