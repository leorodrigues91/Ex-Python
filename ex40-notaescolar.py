cores = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'verde':'\033[1:32m',
         'amarelo': '\033[1:33m',
         'cls': '\033[m'}
print(f'{cores["amarelo"]}-={cores["cls"]}' * 15)
print(f"{cores['red']}{'ANALISADOR DE NOTA ESCOLAR':^30}{cores['cls']}")
print(f'{cores["amarelo"]}-={cores["cls"]}' * 15)
nome = input('Digite o nome do(a) aluno(a): ')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
med = (n1 + n2) / 2
print(f'As notas de {nome} foram: {n1:.1f} e {n2:.1f}.')
print(f'Sua média é: {med:.1f}.')
if med >= 7:
    print(f'{cores["verde"]}{nome} está aprovado(a)! Parabéns!{cores["cls"]}')
elif med > 5 and med < 6.9:
    print(f'{cores["amarelo"]}{nome} está de recuperação!!{cores["cls"]}')
elif med < 5:
    print(f'{cores["red"]}{nome} está reprovado(a)!! Se esforce mais!{cores["cls"]}')
