cores = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'verde':'\033[1:32m',
         'amarelo': '\033[1:33m',
         'negrito': '\033[1m',
         'cls': '\033[m'}
print(f'{cores["amarelo"]}-={cores["cls"]}' * 25)
print(f"{cores['verde']}{'VALIDANDO EXPRESSÕES MATEMÁTICAS':^50}{cores['cls']}")
print(f'{cores["amarelo"]}-={cores["cls"]}' * 25)
exp = str(input('DIGITE A EXPRESSÃO MATEMÁTICA: '))
pilha = []
for simb in exp:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('SUA EXPRESSÃO ESTÁ VÁLIDA!')
else:
    print('SUA EXPRESSÃO ESTÁ INCORRETA!')
