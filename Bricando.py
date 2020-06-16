print('testandooo......')
print('-='*20)
ano=int(input('Em que ano você nasceu? '))
soma=0
idade=ano
soma_idade=ano-idade

while soma ==0:
    if idade < 2002:
        print('Você tem {} anos,é de maior!'.format(soma_idade))
        soma+=1
    else:
        print('Você tem {} anos,é de menor'.format(soma_idade))
        soma=+1
print('FIM')