conjunto=[]
sair='N'
maior=0
while sair !='S':
    num=int(input('Digite um numero:'))
    if num<0 or num>1000:
        print('Numero invalido!')
        continue
    else:
        conjunto.append(num)
        testeMenor=num
    if num>=maior:
        maior=num
    sair=str.upper(input('Digite S para sair, outra tecla continua: '))

i=0
soma=0
menor=1001
for i in range (0,len(conjunto)):
    soma=conjunto[i]+soma
    if conjunto[i]<menor:
        menor=conjunto[i]

print(conjunto)
print('Soma: {} '.format(soma))
print('Menor: {}'.format(menor))
print('Maior: {}'.format(maior))