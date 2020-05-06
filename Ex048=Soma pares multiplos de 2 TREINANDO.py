soma=0
cont=0
for n in range(2,51, 2):
    print(n,end=(' '))
    if n %2 ==0:
        soma=soma+n
        cont=cont+1
print('\nA soma dos valores {} solicitados é {}'.format(cont,soma))










