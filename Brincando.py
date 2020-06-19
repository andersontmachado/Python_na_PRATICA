from time import sleep
from datetime import date
print('testandooo......')
print('-='*20)
atual=date.today().year
ano=int(input('Em que ano você nasceu? '))
soma=0
opção=0
maior=0
idade=atual-ano
while soma ==0:
    if idade <= 17:
        sleep(2)
        print('Você tem \033[32m{}\033[m anos,é de menor!'.format(idade))
        soma+=1
    else:
        sleep(2)
        print('Você tem \033[31m{}\033[m anos,é de maior!'.format(idade))
        soma+=1
while opção !=5:
    print('''    [1]Balada
    [2]Igreja
    [3]Futebol
    [4]Escola
    [5]Sair''')
    opção=int(input('Qual sua opção:'))
    if opção ==1 and idade>=18:
        print('Você tem {} anos,pode ir!'.format(idade))
        maior+=1
    else:
        print('Você tem {} anos,é um bebe ainda,não pode sair!'.format(idade))


print('FIM...')









