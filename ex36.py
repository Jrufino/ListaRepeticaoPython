'''Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário,
mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, 
valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:
Montar a tabuada de: 5
Começar por: 4
Terminar em: 7

Vou montar a tabuada de 5 começando em 4 e terminando em 7:
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
Obs: Você deve verificar se o usuário não digitou o final menor que o inicial'''

num=int(input('Digite o numero que deseja saber a tabuada: '))
valorInicial=int(input('Digite o valor inicial: '))
valorFinal=int(input('Digite o valor final:'))

if valorInicial> valorFinal:
    print('Valor final maior que o valor inicial.')

print('Montar a tabuada de: {}'.format(num))
print('Começar por:{}'.format(valorInicial))
print('Começar por:{}'.format(valorFinal))

i=valorInicial
for i in range(valorInicial,valorFinal+1):
    print('{0} X {1} = {2}'.format(num,i,num*i))
    i=valorInicial+1