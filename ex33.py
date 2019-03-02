'''O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa
que leia as um conjunto indeterminado de temperaturas,
e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.'''

temperaturas=[]
maior=-999999999999
menor=9999999999999
somaTemperaturas=0
coleta=True

while coleta==True:
    temp=float(input('Digite a temperatura:'))
    temperaturas.append(temp)
    somaTemperaturas=somaTemperaturas+temp
    if temp>maior:
        maior=temp
    if temp<menor:
        menor=temp
    sair=str.upper(input('S-para sair, outra tecla contina:'))
    if sair=='S':
        coleta=False
    else:
        continue

media=somaTemperaturas/len(temperaturas)

print('Menor temperatura: {0:.2f}'.format(menor))
print('Maior temperatura: {0:.2f}'.format(maior))
print('Media das temperaturs: {0:.2f}'.format(media))