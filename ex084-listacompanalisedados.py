cores = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'verde':'\033[1:32m',
         'amarelo': '\033[1:33m',
         'negrito': '\033[1m',
         'cls': '\033[m'}
print(f'{cores["amarelo"]}-={cores["cls"]}' * 25)
print(f"{cores['verde']}{'LISTA COMPOSTA E ANÁLISE DE DADOS':^50}{cores['cls']}")
print(f'{cores["amarelo"]}-={cores["cls"]}' * 25)
pessoas = []
dados = []
peso = []
tot = maior = menor = 0
while True:
    dados.append(str(input('NOME: ').strip().upper()))
    dados.append(float(input('PESO: ').strip()))
    pessoas.append(dados[:])
    peso.append(dados[1])
    tot += 1
    dados.clear()
    resp = str(input('QUER CONTINUAR? [S/N] ').strip().upper())
    if resp in 'Nn':
        break
print('-' * 50)
print(f'VOCÊ CADASTROU {tot} PESSOAS.')
for p in pessoas:
    if p[1] == max(peso):
        maior = p[1]
    if p[1] == min(peso):
        menor = p[1]
print(f'O MAIOR PESO FOI DE {maior:.2f} Kg. Peso de', end=' ')
for i, pesos in pessoas:
    if pesos == maior:
        print(f'{i} ', end='')
print()
print(f'O MENOR PESO FOI DE {menor:.2f} Kg. Peso de', end=' ')
for i, pesos in pessoas:
    if pesos == menor:
        print(f'{i} ', end='')
print()
