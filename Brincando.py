from time import sleep
from datetime import date
from random import randint
print('testandooo......')
print('-='*20)
atual=date.today().year
nome=str(input('Digite seu nome: ')).strip().upper()
sobre=str(input('Digite seu sobrenome: ')).strip().upper()
print('Seu nome é {} {}'.format(nome,sobre))
ano=int(input('Em que ano você nasceu? '))
soma=opção=cont=0
idade=atual-ano
cat=ano
exame=aluno=''
while opção !=99:
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
    [5]Jogos
    [99]Sair''')
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
    elif opção ==4:
        aluno=str(input('Você ainda estuda?[S/N]').strip().upper()[0])
        if aluno in 'Nn' and idade <18:
            idade=atual-ano
            print('Você tem \033[32m{}\033[m anos, tem tempo ainda de estudar!'.format(idade))
        elif aluno in 'Nn'and idade >=18:
            print('Você tem \033[31m{}\033[m anos, ta um vagabundo!'.format(idade))
        elif aluno in 'Ss'and idade <18:
            print('Você tem {} anos e ainda está \033[34mESTUDANDO!\033[m'.format(idade))
        elif aluno in 'Ss'and idade >=18:
            print('Você tem \033[33m{}\033[m anos e já pode cursar uma faculdade!'.format(idade))
    elif opção ==5:
        itens='PEDRA','PAPEL','TESOURA'
        computador=randint(0,2)
        print('''Digite a opção
                [0]PEDRA
                [1]PAPEL
                [2]TESOURA''')
        jogada=int(input('Qual sua jogada: '))
        print('O jogador jogou {}'.format(itens[jogada])
        print('O computador jogou {}'.format(itens[computador])















print('FIM')




