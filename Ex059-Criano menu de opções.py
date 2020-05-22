n1=int(input('Digite o primeiro valor: '))
n2=int(input('Digite o segundo valor: '))
opção=0
while opção !=5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos Números
    [ 5 ] Sair do Programa''')
    opção=int(input('>>>>>Qual sua opção: '))
    if opção == 1:
        soma=n1+n2
        print('A soma entre {} + {} é {}'.format(n1,n2,soma))
    elif opção == 2:
        multi=n1*n2
        print('A multiplicação de {} X {} é {}'.format(n1,n2,multi))
    elif opção == 3:
      if n1>n2:
        maior=n1
      else:
        maior=n2
        print('O maior valor de {} e {} é {}'.format(n1,n2,maior))
    elif opção == 4:
        print('Infome os números novamente:')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Dados Inválidos,tente novamente!')
print('-='*12)
print('Programa finalizado!')






























