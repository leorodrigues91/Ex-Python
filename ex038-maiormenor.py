cores = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'amarelo': '\033[1:33m',
         'cls': '\033[m'}
v1 = int(input('Digite o primeiro número: '))
v2 = int(input('Digite o segundo número: '))
if v1 > v2:
    print(f'O {cores["azul"]}primeiro valor{cores["cls"]} é maior.')
elif v2 > v1:
    print(f'O {cores["azul"]}segundo valor{cores["cls"]} é maior.')
elif v1 == v2:
    print(f'Não existe valor maior. {cores["azul"]}Os dois são iguais{cores["cls"]}.')
