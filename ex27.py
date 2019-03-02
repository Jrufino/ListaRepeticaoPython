'''Faça um programa que calcule o número médio de alunos por turma. 
Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. 
As turmas não podem ter mais de 40 alunos.'''


qtdTurmas=int(input('Digite a quantidade de turmas disponiveis: '))
somaAlunos=0
turmas=[]

i=0
for i in range (0, qtdTurmas):
    qtdAlunos=int(input('Digite a quantidade de alunos da turma: '))
    if qtdAlunos>40:
        print('Quantidade invalida')
        continue
    else:
        turmas.append(qtdAlunos)
        somaAlunos=somaAlunos+qtdAlunos

mediaAlunos=somaAlunos/len(turmas)

print('Media de alunos da escola por turma: {} alunos'.format(mediaAlunos))