print('-' * 40)
print(f"{'ANALISADOR DE AUMENTO SALARIAL':^40}")
print('-' * 40)
sal = float(input('Digite o salário: R$ '))
if (sal > 1250.00):
    aumento = sal * 0.10
    print(f'Você receberá um aumento de 10%.')
    print(f'Seu novo salário será: R$ {sal + aumento:.2f}')
if (sal <= 1250.00):
    aumento = sal * 0.15
    print(f'Você receberá um aumento de 15%.')
    print(f'Seu novo salário será: R$ {sal + aumento:.2f}')
