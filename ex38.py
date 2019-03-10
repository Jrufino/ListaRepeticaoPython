'''Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. 
Faça um programa que determine o salário atual desse funcionário. 
Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.'''

anoInicial=1995
salarioInicial=float(input('Digite o salario inicial:'))
taxaAumento=0
anoAtual=int(input('Digite o ano atual:'))

anoSeguinte=anoInicial+1
taxaAumento=0.015
salarioAtual=salarioInicial+salarioInicial*taxaAumento

for i in range(anoSeguinte, anoAtual):
    taxaAumento=taxaAumento*2
    salarioAtual=salarioAtual+salarioAtual*taxaAumento
    

print('Salario Atual: ${0:.2f}'.format(salarioAtual))
print('Taxa de aumento em relacao ao ano anterior:{0:.2f}'.format(taxaAumento))
