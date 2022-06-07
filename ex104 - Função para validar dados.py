#    Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante
#    à função input() do Python, só que fazendo a validação para aceitar
#    apenas um valor numérico.

#   FUNÇÕES UTILIZADAS NA ESTÉTICA DO PROGRAMA
cor = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'verde':'\033[1:32m',
         'amarelo': '\033[1:33m',
         'negrito': '\033[1m',
         'cls': '\033[m'}
def título(txt):
    print(f'{cor["amarelo"]}-={cor["cls"]}' * 25)
    print(f"{cor['verde']}{txt:^50}{cor['cls']}")
    print(f'{cor["amarelo"]}-={cor["cls"]}' * 25)

#   CABEÇALHO APENAS PARA EFEITOS VISUAIS
título('FUNÇÕES PARA VALIDAR DADOS')

#   INÍCIO DO PROGRAMA


def leiaInt(n):
    while not n.isnumeric():
        print(f'{cor["red"]}ERRO! DIGITE UM NÚMERO INTEIRO VÁLIDO!{cor["cls"]}')
        n = input('Digite um número: ')
    return n


num = leiaInt(input('Digite um número: '))
print(f'Você digitou o número {cor["azul"]}{num}{cor["cls"]}')

'''n = leiaInt('Digite um número: ')
print(n)'''
