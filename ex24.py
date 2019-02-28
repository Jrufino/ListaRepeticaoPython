sair='N'
notas=[]
while sair !='S':
    nota=float(input('Insira uma nota valida: '))
    if nota<0 or nota>10:
        print('Nota invalida!')
        continue
    else:
        notas.append(nota)
    i=0
    somaNotas=0
    for i in range(len(notas)):
        somaNotas=somaNotas+notas[i]
    media=(somaNotas/len(notas))
    print('Media {0:.2f}'.format(media))