#   Faça um programa que tenha uma função notas() que pode receber várias notas
#   de alunos e vai retornar um dicionário com as seguintes informações:
#   1) Quantidade de notas; 2) A maior nota; 3) A menor nota;
#   4) A média da turma; 5) A situação (opcional).

#   FUNÇÕES UTILIZADAS NA ESTÉTICA DO PROGRAMA
cor = {'azul': '\033[1:34m',
         'red': '\033[1:31m',
         'verde':'\033[1:32m',
         'amarelo': '\033[1:33m',
         'negrito': '\033[1m',
         'cls': '\033[m'}
def título(txt):
    print(f'{cor["amarelo"]}-={cor["cls"]}' * 25)
    print(f"{cor['verde']}{txt:^50}{cor['cls']}")
    print(f'{cor["amarelo"]}-={cor["cls"]}' * 25)

#   CABEÇALHO APENAS PARA EFEITOS VISUAIS
título('FUNÇÃO DICIONÁRIO COM NOTAS DE ALUNOS')

#   INÍCIO DO PROGRAMA

def notas(*n, sit=False):
    '''
    -> Função para analisar as notas e situaçãoes de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional que irá mostrar ou não a situação dos alunos.
    :return: dicionário com informações sobre os alunos.
    '''

    aluno = dict()
    aluno['total'] = f'{len(n)} notas'
    aluno['maior'] = max(n)
    aluno['menor'] = min(n)
    aluno['média'] = sum(n) / len(n)
    if sit:
        if aluno['média'] >= 7:
            aluno['situação'] = 'BOA'
        elif aluno['média'] >= 5:
            aluno['situação'] = 'RAZOÁVEL'
        else:
            aluno['situação'] = 'RUIM'
    return aluno

resp = notas(5.5, 2.5, 9, 8.5, sit=True)
print(resp)

'''while True:
    n1.append(float(input(f'INSIRA A {i}ª NOTA: ')))
    if i == 4:
        break
    while True:
        resp = str(input('Deseja continuar? [S/N] ').strip().upper())
        if resp == 'S' or resp == 'N':
            break
        print(f'{cor["red"]}OPÇÃO INVÁLIDA! UTILIZE APENAS "S" OU "N".{cor["cls"]}')
    if resp == 'N':
        break
    i += 1'''
'''media = sum(nota) / len(nota)
print(nota)
print(media)'''
