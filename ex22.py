sair='N'
divisivel=[]
while sair !='S':
    num=int(input('Digite um numero inteiro: '))

    if num==2 or num==3 or num==5 or num==7:
        print('Primo')
    else:
        if num%2==0 or num%3==0 or num%5==0 or num%7==0:
            if num%2==0:
                divisivel.append(2)
            if num%3==0:
                divisivel.append(3)
            if num%5==0:
                divisivel.append(5)
            if num%7==0:
                divisivel.append(7)
            print('Nao eh primo. Divisivel por {}'.format(divisivel))
        else:
            print('Primo')
    sair=str.upper(input('S- Sair, outra tecla continua'))