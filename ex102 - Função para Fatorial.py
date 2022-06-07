#   Crie um programa que tenha uma função chamada "fatorial()"
#   que receba dois parâmetros: o primeiro que indique o número a calcular
#   e o outro chamado show, que será o valor lógico (opcional)
#   indicando se será mostrado ou não na tela o processo de cálculo fatorial.

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
título('FUNÇÕES PARA FATORIAL')

#   INÍCIO DO PROGRAMA

def fatorial(n=1, show=False):
    '''
    -> Função que calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostra ou não o cáculo do fatorial.
    :return: O resultado do fatorial de um número "n".
    '''
    f = 1
    count = n
    while count > 0:
        if show == True:
            print(f'{count}', end='')
            print(' x ' if count > 1 else ' = ', end='')
            f *= count
            count -= 1
        else:
            f *= count
            count -= 1
    return f

num = int(input('INSIRA O NÚMERO PARA CALCULAR O FATORIAL: '))
calc = str(input('DESEJA MOSTRAR O CÁCULO JUNTO DO RESULTADO [S/N]? ').strip())
if calc in 'Ss':
    calc = True
else:
    calc = False
print(f'{fatorial(num, calc)}')
#help(fatorial)