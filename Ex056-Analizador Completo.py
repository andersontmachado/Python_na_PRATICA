somaidade=0
médiaidade=0
maioridadehomem=0
nomevelho=''
totmulher=0
for p in range(1,5):
    print('------{}ªpessoa------'.format(p))
    nome=str(input('NOME: ')).strip()
    idade=int(input('IDADE: '))
    sexo=str(input('M/F: '))
    somaidade=somaidade+idade
    if p == 1 and sexo in 'Mn':
        maioridadehomem=idade
        nomevelho=nome
    if sexo in 'Mn' and idade>maioridadehomem:
        maioridadehomem=idade
        nomevelho=nome
    if sexo in 'Fm' and idade <20:
        totmulher=totmulher+1

médiaidade=somaidade/4
print('A média de idade do grupo é {}'.format(médiaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem,nomevelho))
print('Ao todo são {} mulheres menor de 20 anos.'.format(totmulher))

























