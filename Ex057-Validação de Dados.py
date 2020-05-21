sexo=str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo=str(input('Dados Inválidos.Por favor,informe seu sexo:')).strip().upper()[0]
print('Sexo \033[32m{}\033[m registrado com sucesso'.format(sexo))
#fiz algumas mudanças,não funciono,então coloquei só somente a cor...







