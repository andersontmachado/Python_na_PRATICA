listagem=('Lapis',1.75,
          'Boracha',2,
          'Caderno',15.90,
          'Estojo',3,
          'Tranferidor',7,
          'Livros',30)
print('='*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('='*40)
for pos in range(0,len(listagem)):
    if pos % 2==0:
        print(f'{listagem[pos]:.<30}',end='')
    else:
        print(f'{listagem[pos]:>7.2f}')



