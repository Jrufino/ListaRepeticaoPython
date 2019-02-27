iteracao=0
maior=0

while iteracao<5:
    num=int(input('Digite um numero: '))
    if num > maior:
        maior=num
    iteracao=iteracao+1

print('O maior numero digitado foi: {}'.format(maior))