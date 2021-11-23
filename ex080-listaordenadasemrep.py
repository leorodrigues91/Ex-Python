cores = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'verde':'\033[1:32m',
         'amarelo': '\033[1:33m',
         'negrito': '\033[1m',
         'cls': '\033[m'}
print(f'{cores["amarelo"]}-={cores["cls"]}' * 25)
print(f"{cores['verde']}{'LISTA ORDENADA SEM REPETIÇÃO':^50}{cores['cls']}")
print(f'{cores["amarelo"]}-={cores["cls"]}' * 25)
valor = []
for c in range(0, 5):
    num = int(input('DIGITE UM VALOR: '))
    if c == 0 or num > valor[-1]:
        valor.append(num)
        print(f'O VALOR FOI ADICIONADO AO FINAL DA LISTA.')
    else:
        pos = 0
        while pos < len(valor):
            if num <= valor[pos]:
                valor.insert(pos, num)
                print(f'O VALOR FOI ADICIONADO NA POSIÇÃO {pos} DA LISTA.')
                break
            pos += 1
print('-' * 50)
print(f'OS VALORES DIGITADOS EM ORDEM FORAM: {valor}')

'''prim, ult = 0, len(valor)
    while prim < ult:
        meio = (prim + ult) // 2
        if num < valor[meio]:
            ult = meio
        else:
            prim = meio + 1
    valor.insert(prim, num)'''