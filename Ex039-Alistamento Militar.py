from datetime import date
print('''Digite a opção:
[1]Feminino
[2]Masculino''')
opcao=int(input('Sua opção: '))
if opcao == 1:
    print('Você é do sexo \033[1;31mFEMININO\033[m,não precisa se \033[4;32mALISTAR.\033[m')
elif opcao ==2:
    print('Você é do sexo \033[1;36mMASCULINO\033[m, precisa se \033[4;33mALISTAR.\033[m')
    atual=date.today().year
    nasc=int(input('Digite o ano de nascimento: '))
    idade=atual-nasc
    print('Quem nasceu em {} tem {} anos em {}'.format(nasc,idade,atual))
    if idade == 18:
        print('Você tem que se alistar URGENTISSIMO!')
    elif idade <18:
        saldo=18-idade
        print('Ainda falta {} anos para se alistar.'.format(saldo))
        ano=atual+saldo
        print('Seu alistamento será em {}'.format(ano))
    elif idade >18:
        saldo=idade-18
        print('Você deveria se alistar há {} anos.'.format(saldo))
        ano=atual-saldo
        print('Seu alistamento foi {}'.format(ano))
else:
    print('Opção invalida,tente outra vez.')


















































