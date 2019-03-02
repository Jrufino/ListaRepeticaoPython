'''Faça um programa que peça para n pessoas a sua idade, 
ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; 
e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.'''

idades=[]
somaIdades=0
sair='N'

while sair!='S':
    idade=int(input('Digite sua idade: '))
    idades.append(idade)
    somaIdades=somaIdades+idade
    sair=str.upper(input('S-Sair, outra tecla continua: '))

media=(somaIdades/len(idades))

if media>0 and media<15:
    print('Turma jovem')
elif media>=25 and media<60:
    print('Turma adulta')
elif media>60:
    print('Turma idosa')

print('Media de idade da turma: {0:.2f}'.format(media))