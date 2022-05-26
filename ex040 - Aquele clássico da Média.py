# Crie um programa que leia quatro notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

i = 1
nota = []

while i <= 4:
    nota.append(float(input(f"Informe a {i}ª nota: ")))
    i += 1

media = sum(nota)/4

print(f"A media do aluno é: {media:.1f}")

if media >= 7:
    print("O aluno está APROVADO!")
elif 5 < media < 6.9:
    print("O aluno está em RECUPERAÇÃO!")
else:
    print("O aluno está REPROVADO!")
