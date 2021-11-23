cores = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'verde':'\033[1:32m',
         'amarelo': '\033[1:33m',
         'negrito': '\033[1m',
         'cls': '\033[m'}
from time import sleep
print(f'{cores["amarelo"]}-={cores["cls"]}' * 20)
print(f"{cores['azul']}{'OPERAÇÕES NUMÉRICAS':^40}{cores['cls']}")
print(f'{cores["amarelo"]}-={cores["cls"]}' * 20)
opcao = 4
num1 = int(input(f'Digite o 1º valor: '))
num2 = int(input(f'Digite o 2º valor: '))
while opcao != 5:
    print('-' * 40)
    print(f'ESCOLHA UMA DAS OPÇÕES ABAIXO:\n'
          f'    {cores["amarelo"]}[ 1 ]{cores["cls"]} SOMAR\n'
          f'    {cores["amarelo"]}[ 2 ]{cores["cls"]} MULTIPLICAR\n'
          f'    {cores["amarelo"]}[ 3 ]{cores["cls"]} MAIOR\n'
          f'    {cores["amarelo"]}[ 4 ]{cores["cls"]} NOVOS NÚMEROS\n'
          f'    {cores["amarelo"]}[ 5 ]{cores["cls"]} SAIR')
    opcao = int(input('ESCOLHA SUA OPÇÃO: '))
    print('-' * 40)
    if opcao == 1:
        soma = num1 + num2
        print(f'A SOMA ENTRE {num1} E {num2} É IGUAL A: {cores["azul"]}{soma}{cores["cls"]}')
    elif opcao == 2:
        mult = num1 * num2
        print(f'A MULTIPLICAÇÃO ENTRE {num1} E {num2} É IGUAL A: {cores["azul"]}{mult}{cores["cls"]}')
    elif opcao == 3:
        maior = num1
        if num2 > num1:
            maior = num2
        print(f'ENTRE {num1} E {num2} O MAIOR VALOR É: {cores["azul"]}{maior}{cores["cls"]}')
    elif opcao == 4:
        print('INFORME NOVOS NÚMEROS.')
        num1 = int(input(f'Digite o 1º valor: '))
        num2 = int(input(f'Digite o 2º valor: '))
    elif opcao == 5:
        print('FINALIZANDO...')
        sleep(1)
        print('FINALIZADO!')
    else:
        print(f'{cores["red"]}OPÇÃO INVÁLIDA!\n'
              f'INFORME APENAS AS OPÇÕES MOSTRADAS NO MENU.{cores["cls"]}')
print('-' * 40)
sleep(1)
print(f'{cores["verde"]}OBRIGADO POR UTILIZAR NOSSO PROGRAMA.\n'
      f'TENHA UM ÓTIMO DIA!{cores["cls"]}')
