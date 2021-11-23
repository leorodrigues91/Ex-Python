preco1 = float(input("Digite o preço do produto: R$ "))
desconto = preco1 * 0.05
preco2 = preco1 - desconto
print('-' * 25)
print(f'Valor original: R$ {preco1:.2f}')
#if (desconto < 1):
#   print(f'Desconto: R$ {desconto:.2f} centavos')
print(f'Desconto: R$ {desconto:.2f}')
print(f'Valor com desconto: R$ {preco2:.2f}')
print('-' * 25)
