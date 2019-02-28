sair='N'
primos=[2,3,5,7]
while sair !='S':
    num=int(input('Digite um numero inteiro: '))
    i=1
    for i in range (1, num):
        if i!=1 and i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0:
            primos.append(i)
        i=i+1    
    print('Primos entre 1 e {}'.format(num))
    print('\n{}'.format(primos))
    print('Quantidade de primos: {}'.format(len(primos)))          
    sair=str.upper(input('S- Sair, outra tecla continua'))
