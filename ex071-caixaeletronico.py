from time import sleep

cores = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'verde': '\033[1:32m',
         'amarelo': '\033[1:33m',
         'negrito': '\033[1m',
         'cls': '\033[m'}
align = {'ctr': f'{"":^15}',
         'cls': f'{"":<0}'}
print(f'{cores["amarelo"]}-={cores["cls"]}' * 25)
print(f"{cores['verde']}{'CAIXA ELETRÔNICO BANCO VIRTUAL':^50}{cores['cls']}")
print(f'{cores["amarelo"]}-={cores["cls"]}' * 25)
saque = int(input('INFORME QUANTO DESEJA SACAR: R$ '))
tmp = 0
print('-' * 50)
print(f'{align["ctr"]}{"ANALISANDO TRANSAÇÃO"}{align["cls"]}', end='')
sleep(0.75)
while tmp < 3:
    print(f'.', end='')
    sleep(0.5)
    tmp += 1
sleep(1)
print(f'\n{"-[ PROCESSANDO CONTAGEM DE CÉDULAS ]-":^50}')
sleep(2)
print('-' * 50)
while True:
    if saque == 0:
        print(f'VALOR DO SAQUE: R$ {saque:.2f}')
        break
    else:
        print(f'CONFIRMANDO VALOR DO SAQUE: R$ {saque:.2f}')
        sleep(1)

        cinq = saque // 50  # CALCULAR CÉDULAS DE 50
        saque -= (cinq * 50)

        vinte = saque // 20  # CALCULAR CÉDULAS DE 20
        saque -= (vinte * 20)

        dez = saque // 10  # CALCULAR CÉDULAS DE 10
        saque -= (dez * 10)

        um = saque  # O RESTANTE SÃO AS NOTAS DE 1 REAL

        if cinq != 0:
            print(f'TOTAL DE {cinq} CÉDULAS DE R$ 50.00')
        if vinte != 0:
            print(f'TOTAL DE {vinte} CÉDULAS DE R$ 20.00')
        if dez != 0:
            print(f'TOTAL DE {dez} CÉDULAS DE R$ 10.00')
        if um != 0:
            print(f'TOTAL DE {um} CÉDULAS DE R$ 1.00')
        break
print('-=' * 25)
print('OBRIGADO POR UTILIZAR NOSSOS SERVIÇOS.\n'
      'TENHA UM ÓTIMO DIA!')
