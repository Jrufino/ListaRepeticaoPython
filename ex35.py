'''Encontrar números primos é uma tarefa difícil.
Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.'''

primos=[]

num=int(input('Digite um numero:'))
numFornecido=num

for i in range (1,num):
    if num%2!=0 and num%3!=0 and num%5!=0 and num%7!=0:
        primos.append(num)
    num=num-1

if numFornecido>7:
    primos.append(2) 
    primos.append(3) 
    primos.append(5) 
    primos.append(7)
elif numFornecido>=5 and numFornecido<7:
    primos.append(2) 
    primos.append(3) 
    primos.append(5) 
elif numFornecido>=3 and numFornecido<5:
    primos.append(2) 
    primos.append(3) 
elif numFornecido>= 2 and numFornecido<3:
    primos.append(2)

primos.sort()

print('Primos entre 1 e {}: {}'.format(numFornecido,primos))