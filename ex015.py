dia = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
valor = (dia * 60) + (km * 0.15)
print(f'O total a pagar é: R$ {valor:.2f}')
