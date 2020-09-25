print('='*30)
print('{:^30}'.format('BANCO ANDERSON'))
print('='*30)
saque=int(input('Qual valor você quer sacar?R$'))
total=saque
céd=100
totalcéd=0
cont=0
while True:
    if total>=céd:
        total-=céd
        totalcéd+=1
    else:
        if totalcéd>0:
            print(f'Total de {totalcéd} cédulas de R${céd}')
        if céd==100:
            céd=50
        elif céd==50:
            céd=20
        elif céd ==20:
            céd=10
        totalcéd=0
        if total ==0:
            break

print('='*50)
print('TESTANDO.....Muito Obrigado por utilizar o BANCO ANDERSON')


