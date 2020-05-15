somaidade=0
mediaidade=0
maioridadehomem=0
nomevelho=''
totmulher=0
for p in range(1,5):
    print('------{}ªpessoa------'.format(p))
    nome=str(input('Nome: ')).strip().upper()
    idade=int(input('Idade: '))
    sexo=str(input('M/F: '))
    somaidade=somaidade+idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem=idade
        nomevelho=nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem=idade
        nomevelho=nome
    if sexo in 'Ff' and idade<20:
        totmulher=totmulher+1


mediaidade=idade/4
print('A media de idade do grupo é {}'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem,nomevelho))
print('Ao todo são {} mulheres menor de 20 anos.'.format(totmulher))









