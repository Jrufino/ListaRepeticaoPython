num=int(input('Digite um numero inteiro: '))
numUsuario=num
fatorial=1

while num>0:
    fatorial=num*fatorial
    num=num-1

print('Fatorial de {}: {}'.format(numUsuario,fatorial))