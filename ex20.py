sair='N'
while sair !='S':
    num=int(input('Digite um numero inteiro: '))
    if num>16:
        print('O numero deve ser menor que 16!')
        continue
    numUsuario=num
    fatorial=1

    while num>0:
        fatorial=num*fatorial
        num=num-1

    print('Fatorial de {}: {}'.format(numUsuario,fatorial))
    sair=str.upper(input('Digite S para sair, outra tecla continua: '))