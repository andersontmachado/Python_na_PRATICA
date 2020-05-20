lgbts=''
sexo=str(input('Informe seu sexo: [M/F ou LGBTS] ')).strip().upper()[0]
while sexo not in 'MFLgbts':
    if sexo in 'LGBTS':
        lgbts=sexo
        print('Você é {} uma bixona!'.format(lgbts))
    sexo=str(input('Dados Inválidos.Por favor,informe seu sexo:')).strip().upper()[0]
print('Sexo \033[32m{}\033[m registrado com sucesso'.format(sexo))





