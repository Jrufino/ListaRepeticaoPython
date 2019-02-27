validade=False

while validade!=True:
    nome=str(input('Digite um nome com mais do que 3 caracteres:'))
    if len(nome)<3:
        print('Nome invalido!')
        continue
    idade=int(input('Digite a idade entre 0 e 150:'))
    if idade<0 and idade>150:
        print('Idade invalida!')
        continue
    salario=float(input('Digite o salario: RS'))
    if salario<0:
        print('Salario invalido')
        continue
    sexo=str.upper(input('Digite o sexo m ou f:'))
    if sexo!='M'and sexo!='F':
        print('Sexo invalido')
        continue
    estadoCivil=str.upper(input('Digite o estado civil "s","c","v" ou "d"'))
    if estadoCivil!='S'and estadoCivil!='C'and estadoCivil!='V'and estadoCivil!='D':
        print('Estado Civil invalido')
        continue
    else:
        validade=True