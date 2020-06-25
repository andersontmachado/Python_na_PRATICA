from time import sleep
from datetime import date
print('testandooo......')
print('-='*20)
atual=date.today().year
ano=int(input('Em que ano você nasceu? '))
soma=0
opção=0
idade=atual-ano
cat=ano
cont=0
while opção !=5:
    while soma==0:
        if idade <18:
            sleep(0)
            print('Você tem \033[32m{}\033[m anos,é de menor!'.format(idade))
            soma=soma+1
        else:
            sleep(0)
            print('Você tem \033[31m{}\033[m anos,é de maior!'.format(idade))
            soma=soma+1
    print('''    [1]Balada
    [2]Igreja
    [3]Futebol
    [4]Escola
    [5]Sair''')
    opção = int(input('Qual sua opção:'))
    nasc = 2020 - cat
    if opção ==1:
        if idade<18:
            falta=18-nasc
            print('Você tem {} anos e ainda não pode sair!'.format(nasc))
            print('Falta ainda {} anos pra fazer 18.'.format(falta))
            print('='*40)
            cont+=1
        elif idade >=18:
            print('Você tem {} anos e a responsabilidade passa a ser sua.'.format(nasc))
            cont+=1



print('FIM')


######

