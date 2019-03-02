'''O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 
e agora possui uma loja de conveniências. Faça um programa que implemente uma caixa registradora rudimentar.
O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias.
Um valor zero deve ser informado pelo operador para indicar o final da compra.
O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu,
para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial,
para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:
Lojas Tabajara 
Produto 1: R$ 2.20
Produto 2: R$ 5.80
Produto 3: R$ 0
Total: R$ 9.00
Dinheiro: R$ 20.00
Troco: R$ 11.00
...'''

produtosComprados=[]
totalCompra=0
continuarRegistro=True

while continuarRegistro==True:
    precoProduto=float(input('Inserir preco do produto:'))
    produtosComprados.append(precoProduto)
    totalCompra=totalCompra+precoProduto
    finalizarCompra=str.upper(input('Deseja finalizar?'))
    if finalizarCompra=='N':
        continue
    else:
        continuarRegistro=False

formaPagamento=str.upper(input('Digite a forma de pagamento- D- debito, C- Credito, E-Especie:'))
nota=int(input('Digite o valor da nota:'))
troco=nota-totalCompra

print('Lojas Tabajara')

i=0
for i in range (0, len(produtosComprados)):
    print('Produto {0}: R${1:.2f}'.format(i+1,produtosComprados[i]))

print('Total: R${0:.2f}'.format(totalCompra))

if formaPagamento=='C':
    print('Credito: {0:.2f}'.format(totalCompra))
elif formaPagamento=='D':
    print('Debito: {0:.2f}'.format(totalCompra))
elif formaPagamento=='E':
    print('Dinheiro: {0:.2f}'.format(nota))
    print('Troco: {0:.2f}'.format(troco))