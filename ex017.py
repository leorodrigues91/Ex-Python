from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hip = hypot(co, ca)
#hip = (ca ** 2 + co ** 2) ** 0.5
print(f'O valor da hipotenusa é: {hip:.2f}')