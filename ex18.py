conjunto=[]
sair='N'
maior=0
while sair !='S':
    num=int(input('Digite um numero:'))
    conjunto.append(num)
    testeMenor=num
    if num>=maior:
        maior=num
    sair=str.upper(input('Digite S para sair, outra tecla continua: '))

i=0
soma=0
menor=999999999999999999999999999999999999999999999999999999999999
for i in range (0,len(conjunto)):
    soma=conjunto[i]+soma
    if conjunto[i]<menor:
        menor=conjunto[i]

print(conjunto)
print('Soma: {} '.format(soma))
print('Menor: {}'.format(menor))
print('Maior: {}'.format(maior))