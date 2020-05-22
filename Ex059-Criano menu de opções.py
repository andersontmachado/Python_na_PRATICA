n1 = int(input('Digito o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opção=0
while opção !=5:
    print('''[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa''')
    opção=int(input('>>>>>>>>Qual sua opção?'))
    if opção == 1:
       soma=n1+n2
       print('A soma de {} + {} é {}'.format(n1,n2,soma))
    elif opção == 2:
        multi= n1*n2
        print('A multiplicação de {} x {} é {}'.format(n1,n2,multi))
    elif opção == 3:
        if n1>n2:
            maior=n1
        else:
            maior=n2
        print('O maior valor entre {} e {} é {}'.format(n1,n2,maior))
    elif opção == 4:
        print('Informe os números novamente: ')
        n1=int(input('Digite o primeiro valor: '))
        n2=int(input('Digite o segundo valor: '))
    elif opção == 5:
        print('Finalizando....')
    else:
        print('Opção Inválida.Tente novamente!')
print('-='*12)
print('FIM DO PROGRAMA!VOLTE SEMPRE')

























