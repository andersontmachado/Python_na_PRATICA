p=float(input('Qual o preço do produto R$'))
des=p-(p*5/100)

print('O produto que custa R${:.2f},na promoção com 5% vai custar R${:.2f}'.format(p,des))

