num=int(input('Digite o n-esesimo termo para Fibonacci: '))
contador=0
n1=1
n2=1
sequencia=[1,1]

while contador<num:
    n3=n2+n1
    n1=n2
    n2=n3
    sequencia.append(n3)
    contador=contador+1

print('Fibonacci no {} termo: {}'.format(num,sequencia[num-1]))
print('Sequencia: ',sequencia[0:-2])