
validade=False

while validade!= True:

    nota=float(input('Digite uma nota entre 1 e 10:'))

    if nota>0 and nota<=10:
        validade=True
    else:
        validade=False
        print('Valor invalido!')

print('Nota digitada: {}'.format(nota))

