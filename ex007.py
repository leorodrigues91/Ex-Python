nome = input('Digite o nome do(a) aluno(a): ')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
med = (n1 + n2) / 2
print(f'As notas de {nome} foram: {n1} e {n2}.')
print(f'Sua média é: {med}.')
if med >= 7:
    print(f'{nome} está aprovado(a)! Parabéns!')
else:
    print(f'{nome} está reprovado(a)! Se esforce mais!')
