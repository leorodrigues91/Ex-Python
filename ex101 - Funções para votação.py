#   Crie um programa que tenha uma função chamada "voto()" que vai receber
#   como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal
#   indicando se a pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.

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
título('FUNÇÕES PARA VOTAÇÃO')

#   INÍCIO DO PROGRAMA

def voto(num):
    from datetime import date
    idade = date.today().year - num
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 18 < idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    elif idade > 65 or 15 < idade < 18:
        return f'Com {idade} anos: VOTO OPCIONAL'

ano = int(input('INFORME O ANO DE NASCIMENTO: '))
print(voto(ano))
