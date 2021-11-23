cores = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'verde':'\033[1:32m',
         'amarelo': '\033[1:33m',
         'negrito': '\033[1m',
         'cls': '\033[m'}
print(f'{cores["amarelo"]}-={cores["cls"]}' * 20)
print(f"{cores['verde']}{'SEQUÊNCIA DE FIBONACCI':^40}{cores['cls']}")
print(f'{cores["amarelo"]}-={cores["cls"]}' * 20)
qnt = int(input('Quantos elementos deseja mostrar: '))
ult = 1
pen = 0
fib = [0, 1]
if (qnt == 1):
    print(fib[0])
elif (qnt == 2):
    print(*fib, sep=' -> ')
else:
    count = 3
    while count <= qnt:
        termo = ult + pen
        fib.append(termo)
        pen = ult
        ult = termo
        count += 1
    print(*fib, sep=' -> ')
