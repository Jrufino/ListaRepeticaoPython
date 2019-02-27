num1=int(input('Digite um numero inteiro: '))
num2=int(input('Digite outro numero inteiro: '))
iteracao=num1
soma=num1

while iteracao <= num2:
    print('{} '.format(iteracao),end="")
    soma=soma+iteracao
    iteracao=iteracao+1

print('A soma dos numeros foi {}'.format(soma-num1))
    