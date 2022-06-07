#   Crie um programa que leia nome, ano de nascimento e carteira de trabalho
#   e cadastre-os (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO,
#   o dicionário receberá também o ano de contratação e o salário.
#   sabendo que o vencedor tirou o maior número do dado. Calcule e acrescente, além da idade,
#   com quantos anos a pessoa vai se aposentar (Considere aposentadoria após 35 anos de trabalho).

#   CABEÇALHO APENAS PARA EFEITOS VISUAIS

cores = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'verde':'\033[1:32m',
         'amarelo': '\033[1:33m',
         'negrito': '\033[1m',
         'cls': '\033[m'}
print(f'{cores["amarelo"]}-={cores["cls"]}' * 25)
print(f"{cores['verde']}{'CADASTRO DE TRABALHADOR':^50}{cores['cls']}")
print(f'{cores["amarelo"]}-={cores["cls"]}' * 25)

#   INÍCIO DO PROGRAMA

from datetime import date

trabalhador = {}

while True:
    trabalhador["Nome"] = str(input('Nome: ').strip().upper())
    trabalhador["Idade"] = int(input('Ano de Nascimento: ').strip())
    trabalhador["CTPS"] = int(input('No. Carteira de Trabalho (0 = não tem): '))
    if trabalhador["CTPS"] == 0:
        break
    else:
        trabalhador["Contratação"] = int(input('Ano de contratação: '))
        trabalhador["Salário"] = float(input('Salário: R$ '))
        break
idade = date.today().year - trabalhador["Idade"]
trabalhador["Idade"] = idade
if trabalhador["CTPS"] != 0:
    aposenta = (35 - (date.today().year - trabalhador["Contratação"])) + idade
    trabalhador["Aposentadoria"] = aposenta
print('-' * 50)
for k, v in trabalhador.items():
    print(f'{k:.<20}: {v}')
