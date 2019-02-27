num=int(input('Digite um numero entre 1 e 10: '))
multiplicador=1

print('Tabuada de {}'.format(num))
while multiplicador<11:
    print('{} X {} = {}'.format(num,multiplicador,num*multiplicador))
    multiplicador=multiplicador+1
    