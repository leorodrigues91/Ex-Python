#   Faça um programa que tenha uma função chamada "escreva()", que receba um texto qualquer
#   como parâmetro e mostre uma mensagem com tamanho adaptável.
#   Ex:
#   escreva('Olá, Mundo!')
#   Saída:
#   ~~~~~~~~~~~~~~
#     Olá, Mundo!
#   ~~~~~~~~~~~~~~

#   FUNÇÕES UTILIZADAS NA ESTÉTICA DO PROGRAMA
cores = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'verde':'\033[1:32m',
         'amarelo': '\033[1:33m',
         'negrito': '\033[1m',
         'cls': '\033[m'}
def título(txt):
    print(f'{cores["amarelo"]}-={cores["cls"]}' * 35)
    print(f"{cores['verde']}{txt:^70}{cores['cls']}")
    print(f'{cores["amarelo"]}-={cores["cls"]}' * 35)

#   CABEÇALHO APENAS PARA EFEITOS VISUAIS
título('PRINT ADAPTÁVEL')

#   INÍCIO DO PROGRAMA

def escreva(txt):
    tam = len(txt) + 4
    print('~' * tam)
    print(f'  {txt}')
    print('~' * tam)

txt = str(input('INSIRA SUA MENSAGEM: ').strip())
escreva(txt)
