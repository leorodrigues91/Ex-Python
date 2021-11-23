dis = int(input('Informe a distância da viagem: '))
if dis <= 200:
    print(f'O valor da sua passagem é de: R$ {dis * 0.5}')
else:
    print(f'O valor da sua passagem é de: R$ {dis * 0.45}')
