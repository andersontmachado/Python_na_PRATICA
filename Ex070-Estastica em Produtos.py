produto=preço=cont=0
totalcompra=0
totmil=0
menorvalor=0
while True:
    produto=str(input('Nome do Produto: '))
    preço=float(input('Preço: R$'))
    opção=' '
    totalcompra=totalcompra+preço
    while opção not in 'SN':
        opção=str(input('Quer continuar: [S/N]').strip().upper()[0])
    if opção == 'N':
        break
    if opção == 'S':
        cont+=1
    if preço >= 1000:
        totmil+=1
    if preço <1000:
        menorvalor

print(f'O total da compra foi de {totalcompra:.2f}')
print(f'Temos {totmil} com mais de R$1.000,00')
print(f'O produto mais barato foi {produto} que custa {preço} ')






