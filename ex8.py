iteracao=0
soma=0

while iteracao<5:
    num=int(input('Digite um numero: '))
    soma=soma+num
    iteracao=iteracao+1

print('A soma dos numeros digitados foi: {}'.format(soma))
print('A media dos numeros digitados foi: {0:.2f}'.format(soma/5))