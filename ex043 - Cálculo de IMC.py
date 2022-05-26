cores = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'verde':'\033[1:32m',
         'amarelo': '\033[1:33m',
         'cls': '\033[m'}
print(f'{cores["amarelo"]}-={cores["cls"]}' * 15)
print(f"{cores['azul']}{'CALCULADORA DE IMC':^30}{cores['cls']}")
print(f'{cores["amarelo"]}-={cores["cls"]}' * 15)
peso = float(input('Informe o seu peso em kg (ex: 50.5): '))
alt1 = int(input('Informe sua altura em cm (ex: 165): '))
alt2 = alt1 / 100
imc = peso / (alt2 * alt2)
print(f'Seu IMC é: {imc:.1f}')
if imc < 18.5:
    print(f'Você está abaixo do peso.')
elif 18.5 <= imc < 25:
    print(f'Você está na faixa de peso ideal.')
elif 25 <= imc < 30:
    print(f'Você está na faixa de sobrepeso.')
elif 30 <= imc <= 40:
    print(f'Você está na faixa de obesidade.')
elif imc > 40:
    print(f'Você está na faixa de obesidade mórbida.')
