from time import sleep
nome = str(input('Digite seu nome completo: ')).strip()
div = nome.split()
#print(div)
print('ANALISANDO O SEU NOME...')
sleep(2)
print(f'Primeiro nome: {div[0].upper()}')
sleep(1)
print(f'Último nome: {div[-1].upper()}')
