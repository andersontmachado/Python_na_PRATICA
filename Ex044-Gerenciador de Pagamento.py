print('{:=^40}'.format('LOJAS GUANABARA'))
preco_de_compra = float(input('Preço das compras:R$'))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro ou cheque
[2] à vista no cartão
[3] 2x cartão
[4] 3x ou mais no cartão''')
opcao = int(input('Digite a opção: '))
if opcao == 1:
    total = preco_de_compra - (preco_de_compra * 10) / 100
elif opcao == 2:
    total = preco_de_compra - (preco_de_compra * 5) / 100
elif opcao == 3:
    total = preco_de_compra
    par = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS.'.format(par))
elif opcao == 4:
    total=preco_de_compra+(preco_de_compra*20/100)
    totparc=int(input('Quantas parcelas?'))
    parcela=total/totparc
    print('Sua compra parcelada em {}x de R${:.2f} COM JUROS'.format(totparc,parcela))
else:
    total=preco_de_compra
    print('Opção Invalida,tente novamente!')
print('Sua compra de R${:.2f},vai custar R${:.2f} no final.'.format(preco_de_compra, total))




