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
exame=''
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
    elif opção==2:
        if idade<10:
            print('Você ainda tem {} anos e sua mãe vai te levar pra igreja!'.format(nasc))
        elif idade>=10:
            print('Você tem {} anos,ja pode decidir qual caminho seguir,Se é de DEUS ou do diabo!'.format(nasc))
    elif opção ==3:
        if idade<10:
            idade=atual-ano
            print('Você tem {} anos e sua Categoria é FRALDINHA!'.format(idade))
        elif idade<20:
            print('Você tem {} anos e sua Categoria INFANTIL.'.format(idade))
        elif idade <35:
            print('Você tem {} anos e sua Categoria é Adulto!'.format(idade))
        elif idade <45:
            print('Você tem {} anos e sua Categoria é Veterano!'.format(idade))
        elif idade <60:
            exame=str(input('Você ja tem exame médico:[S/N]')).strip().upper()[0]
            if exame not in 'Nn':
                print('Você está apto para participar do CAMPEONATO!')
            else:
                print('Tem que providenciar o exame!')
                print('NÃO PODE JOGAR!')
                print('='*30)





print('FIM')




