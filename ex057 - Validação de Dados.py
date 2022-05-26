cores = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'verde':'\033[1:32m',
         'amarelo': '\033[1:33m',
         'negrito': '\033[1m',
         'cls': '\033[m'}
print(f'{cores["amarelo"]}-={cores["cls"]}' * 20)
print(f"{cores['verde']}{'VALIDAÇÃO DE DADOS':^40}{cores['cls']}")
print(f'{cores["amarelo"]}-={cores["cls"]}' * 20)
sexo = []
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Informe o sexo [M/F]: ').upper().strip()[0])
    if sexo != 'M' and sexo != 'F':
        print('Opção inválida! Por favor, digite apenas "M" ou "F".')
print(f'{cores["verde"]}Obrigado pela informação!{cores["cls"]}')
