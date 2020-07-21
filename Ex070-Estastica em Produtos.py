produto=preço=cont=0
while True:
    produto=str(input('Nome do Produto: '))
    preço=float(input('Preço: R$'))
    opção=' '
    while opção not in 'SN':
        opção=str(input('Quer continuar: [S/N]').strip().upper()[0])
    if opção == 'N':
        break
    if opção == 'S':
        cont+=1


print('Acabo')


