vel = float(input('Digite a velocidade do seu carro: '))
lim = 80
if vel > lim:
    print(f'Velocidade acima do limite permitido, de {lim}km/h.')
    print(f'O valor da sua multa é de: R$ {(vel - lim) * 7:.2f}')
else:
    print('Velocidade dentro do limite permitido. Continue assim e dirija com segurança.')
