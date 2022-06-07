#   Crie um programa que tenha uma função chamada "ficha()", que receba
#   dois parâmetros opcionais: Nome de um jogador e quantos gols ele marcou.
#
#   O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que
#   algum dado não tenha sido informado.

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

def ficha(nome=None, gols=None):
    '''
    -> FUNÇÃO PARA FICHA DE JOGADOR, MOSTRANDO NA TELA O NOME E
    A QUANTIDADE DE GOLS FEITA NO CAMPEONATO.

    :param nome: NOME DO JOGADOR
    :param gols: QUANTIDADE DE GOLS NO CAMPEONATO
    :return: IMPRESSÃO DA FICHA
    '''
    if not nome:
        nome = "<DESCONHECIDO>"
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    return f'O jogador {nome} fez {gols} GOL(S) no campeonato.'

n = str(input('NOME DO JOGADOR: ').strip().upper())
g = str(input('QUANTIDADE DE GOLS: ').strip())

print(ficha(n, g))
