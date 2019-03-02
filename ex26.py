'''Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.'''

candidatoUm=[]
candidatoDois=[]
candidatoTres=[]

numEleitores=int(input('Digite o numero de eleitores: '))
i=0
for i in range (0,numEleitores):
    voto=int(input('Digite seu voto, candidato 1, 2 ou 3:'))
    if voto==1:
        candidatoUm.append(voto)
    elif voto==2:
        candidatoDois.append(voto)
    elif voto==3:
        candidatoTres.append(voto)
    else:
        print('Voto invalido')
        continue

print('Resultado da eleicao: ')
print('Candidato 1: {} votos'.format(len(candidatoUm)))
print('Candidato 2: {} votos'.format(len(candidatoDois)))
print('Candidato 3: {} votos'.format(len(candidatoTres)))