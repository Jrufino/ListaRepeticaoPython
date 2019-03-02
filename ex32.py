'''Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120'''

num=int(input('Digite um numero inteiro:'))
fatorial=1
numeros=[]

while num>0:
    fatorial=num*fatorial
    numeros.append(num)
    num=num-1

print('Fatorial de {}'.format(numeros[0]))
print('{}!='.format(numeros[0]),end="")

i=0
for i in range (0, len(numeros)-1):
    print('{}.'.format(numeros[i]),end="")

print('1={}'.format(fatorial))

