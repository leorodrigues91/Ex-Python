#   Crie um programa que receba valores pelo teclado e gere uma matriz 3x3. Depois mostre a matriz na tela.
#   Mostre também a soma dos valores pares, a soma dos valores da terceira coluna
#   E o maior valor da segunda linha.

#   CABEÇALHO APENAS PARA EFEITOS VISUAIS
cores = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'verde':'\033[1:32m',
         'amarelo': '\033[1:33m',
         'negrito': '\033[1m',
         'cls': '\033[m'}
print(f'{cores["amarelo"]}-={cores["cls"]}' * 25)
print(f"{cores['verde']}{'MATRIZ EM PYTHON - APRIMORADO':^50}{cores['cls']}")
print(f'{cores["amarelo"]}-={cores["cls"]}' * 25)

#   INÍCIO DO PROGRAMA
matriz = [[], [], []]
somapar = somacol = maior = 0
for lc in range(3):
    matriz[lc] = [0] * 3
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'DIGITE UM VALOR PARA {[l, c]}: '))
print('-' * 50)
for linha in matriz:
    for num in linha:
        print(f'[  {num}  ]', end='')
        # SOMANDO OS NÚMEROS PARES
        if num % 2 == 0:
            somapar += num
    print()

# SOMA DA TERCEIRA COLUNA
for lin in range(0,3):
    somacol += matriz[lin][2]

# DESCOBRIR O MAIOR VALOR DA SEGUNDA LINHA
for col in range(0,3):
    if col == 0:
        maior = matriz[1][col]
    elif matriz[1][col] > maior:
        maior = matriz[1][col]

print('-' * 50)
print(f'A SOMA DOS VALORES PARES É: {somapar}')
print(f'A SOMA DOS VALORES DA TERCEIRA COLUNA É: {somacol}')
print(f'O MAIOR VALOR DA SEGUNDA LINHA É: {maior}')

# OUTRA MANEIRA DE DESCOBRIR O MAIOR VALOR DA SEGUNDA LINHA:
# print(f'O MAIOR VALOR DA SEGUNDA LINHA É: {max(matriz[1])}')
