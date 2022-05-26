print('-=' * 15)
print(f"{'ANALISADOR DE TRIÂNGULOS':^30}")
print('-=' * 15)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if ((b - c) < a < b + c) and ((a - c) < b < a + c) and ((a - b) < c < a + b):
    print(f'Os segmentos informados PODEM formar um triângulo.')
else:
    print(f'Os segmentos informados NÃO PODEM formar um triângulo')
