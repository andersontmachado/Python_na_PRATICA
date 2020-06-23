from time import sleep
from datetime import date
print('testandooo......')
print('-='*20)
atual=date.today().year
ano=int(input('Em que ano você nasceu? '))
soma=0
opção=0
maior=0
menor=0
idade=atual-ano
cat=ano
cont=0
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
    nasc=2020-cat
    if opção ==1 and idade>=18:
        print('Você tem {} anos,pode ir!'.format(nasc))
        maior+=1
    elif opção ==1 and idade<18:
        print('Você tem {} anos,é um bebe ainda,não pode sair!'.format(nasc))
        menor=menor+1
    elif opção ==2 and idade <10:
        print('A sua mãe vai te levar pra conhecer a palavra do senhor!')
        menor+=1
    while opção ==3:
        while cont==0:
            if idade < 10:
                print('Você nasceu em \033[31m{}\033[me tem \033[32m{}\033[manos'.format(cat,idade))
                print('Categoria Fraldinha!')
                cont+=1
            elif idade > 10 and idade <20:
                print('Você nasceu em \033[31m{}\033[m e tem \033[32m{}\033anos'.format(cat,idade))
                print('Categoria Pré mirim!')
                cont+=1
            elif idade>20 and idade <35:
                print('Você nasceu em \033[31m{}\033[m e tem \033[31m{}\033[m anos'.format(cat,idade))
                print('Categoria Infantil')
                cont+=1
            elif idade >35 and idade <45:
                print('Você nasceu em \033[31m{}\033[m e tem \033[m{} anos'.format(cat,idade))
                print('Categoria Adulto')
                cont+=1

                print('FIM')
print('ACABOOOOOOOO')
##esse projeto estou desenvolvendo para que eu possa aprender o basico da programação.
##Esse projeto foi para o GIT HUB



