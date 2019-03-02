'''O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha,
que já é um sucesso na sua loja de 1,99. 
Você foi contratado para desenvolver o programa que monta a tabela de preços de pães,
 de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:
Preço do pão: R$ 0.18
Panificadora Pão de Ontem - Tabela de preços
1 - R$ 0.18
2 - R$ 0.36
...
50 - R$ 9.00'''

validadeQuantidade=False
paes=[]

while validadeQuantidade!=True:
    qtdPaes=int(input('Digite a quantidade de paes: '))
    if qtdPaes>50:
        print('Quantidade invalida')
        continue
    else:
        validadeQuantidade=True

i=0
for i in range (0,qtdPaes):
    precoPao=float(input('Digite o preco do pao: '))
    paes.append(precoPao)

print('Panificadora Pão de Ontem - Tabela de preços')

j=0
for j in range(0,qtdPaes):
    print('{0}-{1:.2f}'.format(j+1,paes[j]))


