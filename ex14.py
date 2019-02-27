iterador=0
pares=[]
impares=[]

while iterador<10:
    num=int(input('Digite um numero inteiro: '))
    if num%2==0:
        pares.append(num)
    else:
        impares.append(num)
    iterador=iterador+1

print(len(pares),'Numeros pares:', pares)
print(len(impares),'Numeros impares:', impares)
        