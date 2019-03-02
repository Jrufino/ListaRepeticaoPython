'''O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. 
Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela que contém o número de itens
que o cliente comprou e ao lado o valor da conta. Desta forma a atendente do caixa precisa apenas contar quantos
itens o cliente está levando e olhar na tabela de preços. Você foi contratado para desenvolver o programa
 que monta esta tabela de preços, que conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo:
 Lojas Quase Dois - Tabela de preços
1 - R$ 1.99
2 - R$ 3.98
...
50 - R$ 99.50'''


i=0
j=0
itens=[]

numeroValido=False
while numeroValido!= True:
    numeroItens=int(input('Digite o numero de itens: '))
    if numeroItens>50:
        print('Quantidade deve ser abaixo de 50')
    else:
        numeroValido=True
    
for i in range (0,numeroItens):
    valorItem=float(input('Digite o valor do item {}: '.format(i+1)))
    itens.append(valorItem)
print('Loja Quase Dois - Tabela de precos')
for j in range (0, numeroItens):
    print('{0} - {1:.2f}'.format(j+1,itens[j]))