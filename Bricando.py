from datetime import date
print('testandooo......')
print('-='*20)
atual=date.today().year
ano=int(input('Em que ano você nasceu? '))
soma=0
idade=atual-ano
while soma ==0:
    if idade <= 17:
        print('Você tem {} anos,é de menor!'.format(idade))
        soma+=1
    else:
        print('Você tem {} anos,é de maior!'.format(idade))
        soma+=1


print('FIM...novovsc')



