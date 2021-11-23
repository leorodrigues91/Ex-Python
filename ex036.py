print('-' * 40)
print(f"{'ANALISADOR DE EMPRÉSTIMO':^40}")
print('-' * 40)
cor = {'limpa':'\033[m',
       'verde':'\033[1:32m',
       'red': '\033[1:31m'}

casa = float(input('Informe o valor da casa: R$ '))
salario = float(input('Informe seu salário: R$ '))
anos = int(input('Informe em quantos anos pretende pagar: '))
qnt_prest = anos * 12
valor_prest = casa / qnt_prest
if salario * 0.3 > valor_prest:
    print(f'{cor["verde"]}Parabéns! Seu empréstimo foi aprovado!!{cor["limpa"]}')
    print(f'O valor das suas parcelas será de: {qnt_prest}x R$ {valor_prest:.2f}')
else:
    print(f'{cor["red"]}Infelizmente, seu empréstimo não foi aprovado.{cor["limpa"]}')