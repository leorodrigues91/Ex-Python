from random import shuffle
alunos = []
while len(alunos) < 4:
        nomes = input('Nome do(a) aluno(a): ')
        alunos.append(nomes)
shuffle(alunos)
print(f'A sequencia de apresentações será esta:\n{", ".join(alunos)}'.upper())
