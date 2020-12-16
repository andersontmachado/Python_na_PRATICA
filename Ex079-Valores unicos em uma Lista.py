'''show=[]
for cont in range(0,3):
    show.append(input('Digite os shows que mais gosta: ').upper())
for c,v in enumerate(show):
    print(f'Artista....',(c+1))
    print('=-'*30)
    print(f'Os shows que mais gosta é \033[0;31m{v}\033[m')
    print('=-'*30)
print('Cheguei ao final da lista')'''
#Exercicio feito para relembrar LISTAS, então improvisei montando shows.
a=[2,4,7,9]
b=a[:]#CÓPIA
b[1]=83#ACRESCENTAMOS O VALOR,dai muda na posição,[1] ou [2] ou [3],a qual voce preferir.
print(f'Lista A: {a}')
print(f'Lista B: {b}')
'''Quando se coloca normal assim, sem o [:](cópia),ele repete as duas listas,para acrescentar o valor,devemos fazer
sempre uma cópia, então para não copiar,colocamos o fatiamento,[:].'''
























