'''Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. 
O usuário deverá informar a quantidade de CDs e o valor para em cada um.'''

cd=[]
valorInvestido=0
qtdCds=int(input('Informe a quantidade de CDs de sua colecao: '))

for i in range (0,qtdCds):
    valorCD=float(input('Informe o valor do CD:'))
    cd.append(valorCD)
    valorInvestido=valorInvestido+valorCD

valorMedio=valorInvestido/len(cd)

print('Valor investido na colecao de CDs: R$ {0:.2f}'.format(valorInvestido))
print('Valor medio por cada CD: R${0:.2f}'.format(valorMedio))
