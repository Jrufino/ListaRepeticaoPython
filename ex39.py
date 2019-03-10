'''Faça um programa que leia dez conjuntos de dois valores,
o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. 
Encontre o aluno mais alto e o mais baixo. 
Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.'''

maisAlto=0
maisBaixo=300
i=0
for i in range(0,10):
    numAluno=int(input('Digite o numero do aluno:'))
    alturaCentimetros=int(input('Digite sua altura em centimetros:'))
    if alturaCentimetros>maisAlto:
        maisAlto=alturaCentimetros
        numeroMaisAlto=numAluno
    if alturaCentimetros<maisBaixo:
        maisBaixo=alturaCentimetros
        numeroMaisBaixo=numAluno

print('Numero do aluno mais alto: {}'.format(numeroMaisAlto))
print('Altura do mais alto: {}'.format(maisAlto))
print('Numero do aluno mais baixo: {}'.format(numeroMaisBaixo))
print('Altura do mais baixo: {}'.format(maisBaixo))