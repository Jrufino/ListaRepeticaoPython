base=int(input('Digite a base:'))
expoente=int(input('Digite o expoente:'))
resultado=base
iteracao=1

if base==0:
    resultado=0
elif base==1:
    resultado=1
elif expoente==0:
    resultado=1
elif expoente==1:
    resultado=base
else:
    while iteracao < expoente:
        resultado= resultado*base
        iteracao=iteracao+1


print('O resultado sera {}'.format(resultado))