sair='N'
while sair !='S':
    num=int(input('Digite um numero inteiro: '))

    if num==2 or num==3 or num==5 or num==7:
        print('Primo')
    else:
        if num%2==0 or num%3==0 or num%5==0 or num%7==0:
            print('Nao eh primo')
        else:
            print('Primo')
    sair=str.upper(input('S- Sair, outra tecla continua'))