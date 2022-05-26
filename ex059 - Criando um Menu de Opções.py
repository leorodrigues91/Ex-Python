# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

num1 = int(input("Primeiro valor: "))
num2 = int(input("Segundo valor: "))

while True:
    print("     [ 1 ] SOMAR\n"
          "     [ 2 ] MULTIPLICAR\n"
          "     [ 3 ] MAIOR\n"
          "     [ 4 ] NOVOS NÚMEROS\n"
          "     [ 5 ] SAIR")
    opcao = int(input(">>>>> ESCOLHA UMA DAS OPÇÕES ACIMA: "))

    if opcao == 1:
        soma = num1 + num2
        print(f"A soma de {num1} e {num2} é igual a: {soma}")
        print("=-=" * 15)
    elif opcao == 2:
        mult = num1 * num2
        print(f"O resultado de {num1} x {num2} é igual a: {mult}")
        print("=-=" * 15)
    elif opcao == 3:
        maior = 0
        if num1 > maior:
            maior = num1
        if num2 > num1:
            maior = num2
        print(f"Entre {num1} e {num2}, o maior valor é {maior}")
        print("=-=" * 15)
    elif opcao == 4:
        print("Infome os número novamente:")
        num1 = int(input("Primeiro valor: "))
        num2 = int(input("Segundo valor: "))
        print("=-=" * 15)
    elif opcao == 5:
        break
print("=-=" * 15)
print("OBRIGADO POR UTILIZAR NOSSO PROGRAMA.\n"
      "VOLTE SEMPRE!")
