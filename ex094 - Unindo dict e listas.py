#   Crie um programa que leia nome, sexo e idade de várias pessoas,
#   guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
#   No final, mostre: A) quantas pessoas foram cadastradas; B) a média de idade
#   C) uma lista com todas as mulheres; D) uma lista com as pessoas com idade acima da média

#   CABEÇALHO APENAS PARA EFEITOS VISUAIS
cores = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'verde':'\033[1:32m',
         'amarelo': '\033[1:33m',
         'negrito': '\033[1m',
         'cls': '\033[m'}
print(f'{cores["amarelo"]}-={cores["cls"]}' * 25)
print(f"{cores['verde']}{'CADASTRO DE PESSOAS':^50}{cores['cls']}")
print(f'{cores["amarelo"]}-={cores["cls"]}' * 25)

#   INÍCIO DO PROGRAMA

pessoa = {}
grupo = []
somaid = 0
while True:
    pessoa["Nome"] = str(input('Nome: ').strip().upper())

    while True:
        pessoa["Sexo"] = str(input('Sexo [M/F]: ').strip().upper())
        if pessoa["Sexo"] == 'M' or pessoa["Sexo"] == 'F':
            break
        print(f'{cores["red"]}OPÇÃO INVÁLIDA! UTILIZE APENAS "M" OU "F".{cores["cls"]}')

    pessoa["Idade"] = int(input('Idade: ').strip())
    somaid += pessoa["Idade"]

    grupo.append(pessoa.copy())

    while True:
        resp = str(input('Quer continuar [S/N]? ').strip().upper())
        if resp == 'S' or resp == 'N':
            break
        print('{cores["red"]}OPÇÃO INVÁLIDA! UTILIZE APENAS "S" OU "N".{cores["cls"]}')
    if resp == 'N':
        break

media = somaid / len(grupo)

print('-' * 50)
print(f'- O grupo tem {len(grupo)} pessoas.')
print(f'- A média de idade é de {media:.2f} anos.')
print(f'- As mulheres cadastradas foram:', end=' ')
for p in grupo:
    if p["Sexo"] == "F":
        print(f'[ {p["Nome"]} ]', end=' ')
print()

print(f'- Lista de pessoas que estão acima da média de idade:')
for p in grupo:
    if p["Idade"] > media:
        print(f'{p["Nome"]:.<15}: {p["Idade"]} anos')

print(f'{"<< ENCERRADO >>":-^50}')
