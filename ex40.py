'''Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. 
Foram obtidos os seguintes dados:
Código da cidade;
Número de veículos de passeio (em 1999);
Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
Qual a média de veículos nas cinco cidades juntas;
Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.'''

cidadeMaisAcidentes=0
cidadeMenosAcidentes=1000000000
somaVeiculos=0
cidadeMenorQueDoisMil=[]

i=0
for i in range(0,5):
    codigoCidade=input('Digite o codigo da sua cidade: ')
    numVeiculos=int(input('Digite o numero de veiculos de passeio:'))
    somaVeiculos=somaVeiculos+numVeiculos
    numAcidentesFatais=int(input('Digite o numero de acidentes fatais:'))
    if numVeiculos<2000:
        cidadeMenorQueDoisMil.append(numAcidentesFatais)
    if numAcidentesFatais>cidadeMaisAcidentes:
        cidadeMaisAcidentes=numAcidentesFatais
        cidadeMaisFatal=codigoCidade
        indiceMaisFatal=cidadeMaisAcidentes/numVeiculos
    if numAcidentesFatais<cidadeMenosAcidentes:
        cidadeMenosAcidentes=numAcidentesFatais
        cidadeMenosFatal=codigoCidade
        indiceMenosFatal=cidadeMenosAcidentes/numVeiculos

somaCidadeMenorQueDoisMil=0
j=0
for j in range (0,len(cidadeMenorQueDoisMil)):
    somaCidadeMenorQueDoisMil=somaCidadeMenorQueDoisMil+cidadeMenorQueDoisMil[j]

mediaDasCinco=somaVeiculos/5
mediaDasCidadesMenosDeDoisMil=somaCidadeMenorQueDoisMil/len(cidadeMenorQueDoisMil)
print('===============================================================================')
print('Cidade com maior indice de acidentes: {}'.format(cidadeMaisFatal))
print('Indice de acidentes por veiculo: {}'.format(indiceMaisFatal))
print('Cidade com menos indice de acidentes: {}'.format(cidadeMenosFatal))
print('Indice de acidentes por veiculo: {}'.format(indiceMenosFatal))

print('===============================================================================')
print('Media de veiculos das cinco cidades: {}'.format(mediaDasCinco))

print('===============================================================================')
print('Media de acidentes das cidades abaixo de dois mil: {}'.format(mediaDasCidadesMenosDeDoisMil))