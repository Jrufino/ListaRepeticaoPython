contador=0
n1=1
n2=1
n3=0
sequencia=[1,1]

while n3<500:
    n3=n2+n1
    n1=n2
    n2=n3
    sequencia.append(n3)
    contador=contador+1

print('Fibonacci:',sequencia[0:-1])
