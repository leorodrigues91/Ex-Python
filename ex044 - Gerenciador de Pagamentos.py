cores = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'verde':'\033[1:32m',
         'amarelo': '\033[1:33m',
         'negrito': '\033[1m',
         'cls': '\033[m'}
print(f'{cores["amarelo"]}-={cores["cls"]}' * 15)
print(f"{cores['verde']}{'PAGAMENTO DE PRODUTO':^30}{cores['cls']}")
print(f'{cores["amarelo"]}-={cores["cls"]}' * 15)
valor_prod = float(input('Informe o valor do produto: R$ '))
print(f'Escolha uma das formas de pagamento abaixo:\n'
      f'[ {cores["verde"]}1{cores["cls"]} ] para pagamento à vista, em dinheiro;\n'
      f'[ {cores["verde"]}2{cores["cls"]} ] para pagamento no cartão;')
pag = int(input('Informe aqui sua escolha: '))
if pag == 1:
    desconto = valor_prod * 0.10
    valor_d = valor_prod - desconto
    print('=' * 60)
    print(f'Para pagamentos à vista, você ganha {cores["azul"]}10%{cores["cls"]} de desconto!')
    print(f'O valor final é: {cores["azul"]}R$ {valor_d:.2f}{cores["cls"]}')
    print(f'Agradecemos a preferência. Tenha um ótimo dia!')
    print('=' * 60)
elif pag == 2:
    parc = int(input('Informe a quantidade de parcelas que pretende pagar: '))
    if parc == 1:
        desconto = valor_prod * 0.05
        valor_d = valor_prod - desconto
        print('=' * 65)
        print(f'Para pagamentos à vista no cartão, você ganha {cores["azul"]}5%{cores["cls"]} de desconto!')
        print(f'O valor final é: {cores["azul"]}R$ {valor_d:.2f}{cores["cls"]}')
        print(f'{cores["negrito"]}Agradecemos a preferência. Tenha um ótimo dia!')
        print('=' * 65)
    elif parc == 2:
        v_parc = valor_prod / 2
        print('=' * 50)
        print(f'Seu pagamento será feito em {cores["azul"]}2x de R$ {v_parc:.2f}{cores["cls"]}.')
        print(f'{cores["negrito"]}Agradecemos a preferência. Tenha um ótimo dia!')
        print('=' * 50)
    elif parc > 2:
        juros = valor_prod * 0.20
        valor_j = valor_prod + juros
        print('=' * 65)
        print(f'Para pagamentos acima de 2 parcelas, será acrescido {cores["red"]}20%{cores["cls"]} de juros.')
        print(f'O valor final é: {cores["red"]}R$ {valor_j}{cores["cls"]}')
        print(f'Valor das parcelas: {parc}x de R$ {valor_j / parc:.2f}')
        print(f'{cores["negrito"]}Agradecemos a preferência. Tenha um ótimo dia!')
        print('=' * 65)
else:
    print(f'{cores["red"]}OPÇÃO INVÁLIDA!\n'
          f'Por favor, escolha uma das opções indicadas anteriormente.')
