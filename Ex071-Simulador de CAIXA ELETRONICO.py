print('='*30)
print('{:^30}'.format('BANCO ANDERSON'))
print('='*30)
saque=int(input('Qual valor você quer sacar?R$'))
total=saque
céd=50
totalcéd=0
while True:
    if total>=céd:
        total-=céd
        totalcéd+=1
    else:
        print(f'Total de {totalcéd} de R${céd}')
        if céd==50:
            céd=20
        elif céd==20:
            céd=10
        elif céd ==10:
            céd=1
        if total ==0:
            break
        print('')


