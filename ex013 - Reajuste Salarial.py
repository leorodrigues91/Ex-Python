salario1 = float(input('Digite o valor do salário: R$ '))
aumento = salario1 * 0.15
salario2 = salario1 + aumento
print('-' * 30)
print(f'Salário original: R$ {salario1:.2f}')
print(f'Aumento recebido: R$ {aumento:.2f}')
print(f'Novo salário:     R$ {salario2:.2f}')
print('-' * 30)
