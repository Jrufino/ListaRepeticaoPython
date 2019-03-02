'''Os números primos possuem várias aplicações dentro da Computação,
por exemplo na Criptografia. Um número primo é aquele que é divisível apenas por um e por ele mesmo.
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.'''

primos=[2,3,5,7]

num=int(input('Digite um numero:'))

if num%2==0 or num%3==0 or num%5==0 or num%7==0:
    print('Numero nao primo')
else:
    print('Numero primo')