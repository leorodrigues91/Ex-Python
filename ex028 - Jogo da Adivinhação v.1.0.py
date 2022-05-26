from random import randint
from time import sleep

print('PENSAREI EM UM NÚMERO ENTRE 0 E 5...')
n = randint(0, 5)
sleep(2)
num = int(input('OK. AGORA TENTE ADIVINHAR QUAL NÚMERO PENSEI: '))
if num == n:
    print(f'PARABÉNS! O NÚMERO QUE PENSEI FOI {n}.')
else:
    print(f'QUE PENA! VOCÊ ESCOLHEU {num}, MAS O NÚMERO QUE PENSEI FOI {n}.')
