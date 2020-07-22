cont = 0
total = 0
totmil = 0
menor = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$'))
    cont = cont + 1  # assim que ele ler o preço,vai começar a contar mais um.
    total +=preço
    if preço > 1000:
        totmil += 1
    if cont == 1:  # isso é,se for o primeiro produto
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto
    opção = ' '
    while opção not in 'SN':
        opção = str(input('Quer continuar: [S/N]').strip().upper()[0])
    if opção == 'N':
        break

print(f'O total da compra foi de {total:.2f}')
print(f'Temos {totmil} com mais de R$1.000,00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f} ')
