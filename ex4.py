ano=1

populacaoA=80000
txCrescA=0.03
populacaoB=200000
txCrescB=0.015

while populacaoA < populacaoB:
    populacaoA=populacaoA+populacaoA*txCrescA
    populacaoB=populacaoB+populacaoB*txCrescB
    ano=ano+1

print('A populacao de A demorara {} anos para ultrapassar a populacao de B'.format(ano))
print('A populacao de A sera {0:.2f} e a populacao de B sera {1:.2f}'.format(populacaoA,populacaoB))
