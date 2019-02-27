senhaValida=False

while senhaValida!=True:

    nome=str(input('Digite um nome de usuario: '))
    senha=str(input('Digite a senha: '))

    if nome==senha:
        validade=False
        print('A senha deve ser diferente do nome!')
    else: 
        senhaValida=True

print('Senha inserida com sucesso.')