n = int(input('Digite um número: '))
mult = 1
print(f'A tabuada de {n} é:')
print('-' * 15)
while(mult <= 10):
    print(f'{n:3} x {mult:2} = {n * mult:2}')
    mult = mult + 1
print('-' * 15)
