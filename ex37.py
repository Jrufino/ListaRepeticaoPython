'''Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto,
o mais baixo, a mais gordo e o mais magro, 
para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código,
sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código.
Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto,
do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes'''

maisAlto=0
maisBaixo=3.0
maisGordo=0
maisMagro=200
codigo=""

while codigo!='0':
    codigo=input('Digite seu codigo:')
    if codigo=='0':
        break
    altura=float(input('Digite sua altura:'))
    peso=float(input('Digite seu peso:'))
    if altura>maisAlto:
        alturamaisAlto=altura
        codigoMaisAlto=codigo
        pesoMaisAlto=peso
    if altura<maisBaixo:
        alturamaisBaixo=altura
        codigoMaisBaixo=codigo
        pesoMaisBaixo=peso
    if peso>maisGordo:
        pesomaisGordo=peso
        codigoMaisGordo=codigo
        alturaMaisGordo=altura
    if peso<maisMagro:
        pesomaisMagro=peso
        codigoMaisMagro=codigo
        alturaMaisMagro=altura

print('Codigo do mais alto: {}'.format(codigoMaisAlto))
print('Altura do mais alto: {}'.format(alturamaisAlto))
print('Peso do mais alto: {}'.format(pesoMaisAlto))

print('Codigo do mais baixo: {}'.format(codigoMaisBaixo))
print('Altura do mais baixo: {}'.format(alturamaisBaixo))
print('Peso do mais baixo: {}'.format(pesoMaisBaixo))

print('Codigo do mais gordo: {}'.format(codigoMaisGordo))
print('Altura do mais gordo: {}'.format(alturaMaisGordo))
print('Peso do mais gordo: {}'.format(pesomaisGordo))

print('Codigo do mais magro: {}'.format(codigoMaisMagro))
print('Altura do mais magro: {}'.format(alturaMaisMagro))
print('Peso do mais magro: {}'.format(pesomaisMagro))

