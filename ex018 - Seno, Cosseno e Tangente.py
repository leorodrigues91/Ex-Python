from math import sin, cos, tan, radians
ang = float(input('Digite o valor do angulo: '))
print(f'O seno de {ang} é: {sin(radians(ang)):.2f}')
print(f'O cosseno de {ang} é: {cos(radians(ang)):.2f}')
print(f'A tangente de {ang} é: {tan(radians(ang)):.2f}')
