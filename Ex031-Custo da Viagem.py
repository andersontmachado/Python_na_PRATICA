'''distancia=float(input('Qual a distância percorrida? '))
print(' A distância que você irá percorrer é de {:.2f} km'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('O preço da sua passagem será de R${:.2f}.'.format(preço))'''

#PODERÁ FAZER TAMBEM EM CONDIÇÃO SIMPLICFICADA

distancia=float(input('Qual a distancia percorrida? '))
print(' A distancia que você irá percorrer é de {:.2f} km.'.format(distancia))
preço=distancia*0.50 if distancia <= 200 else distancia*0.45
print('\033[1;31m O preço da sua passagem será de\033[m \033[1;36m R${:.2f} \033[m'.format(preço))
resultado = preço % 2
if resultado == 0:
    print('O numero {:.2f} é PAR'.format(preço))
else:
    print('O número {:.2f} é IMPAR'.format(preço))
if distancia <=200:
    print('Você estará na cidade de SÃO PAULO!'.format(distancia))
else:
    print('Você foi para fora de São Paulo'.format(distancia))

#FIQUEI BRINCANDO COM OS CODIGO PARA APRENDER.MUITO BOM






#EXISTE ESSAS DUAS FORMAR DE FAZER,EU PREFIRO A PRIMEIRA,O CODIGO FICA MAIS FACIL DE LER.
#essas cores eu implementei para aprender bastante.






