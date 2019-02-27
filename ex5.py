
validacao=False

while validacao != True:
    populacaoA=float(input('Informe a populacao de A:'))
    if populacaoA<0:
        print('Digite uma populacao maior do que 0!')
        validacao=False
        continue
    txCrescA=float(input('Informe a taxa de crescimento de A:'))
    populacaoB=float(input('Informe a populacao de B:'))
    if populacaoB <0:
        print('Digite uma populacao maior do que 0!')
        validacao=False
        continue
    txCrescB=float(input('Informe a taxa de crescimento de B:'))
    validacao = True
ano=1

while populacaoA <= populacaoB:
    populacaoA=populacaoA+populacaoA*txCrescA
    populacaoB=populacaoB+populacaoB*txCrescB
    ano=ano+1

print('A populacao de A demorara {} anos para ultrapassar a populacao de B'.format(ano))
print('A populacao de A sera {0:.2f} e a populacao de B sera {1:.2f}'.format(populacaoA,populacaoB))