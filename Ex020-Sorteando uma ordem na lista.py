import random
n1=str(input('Primeiro aluno: '))
n2=str(input('Segundo aluno: '))
n3=str(input('Terceiro aluno: '))
n4=str(input('Quarto aluno: '))
lista=[n1,n2,n3,n4]
embaralhar=random.shuffle(lista)
print('O aluno escolhido foi {}'.format(lista))

#Nessas duas formas dá
#random.shuffle(lista)
#print('A ordem de apresetação será ')
#print(lista)

#quase o mesmo do anterior,colocar só importanto o from random import shuflle
#shuflle é embaralhar#



#random em ingles é aleatorio

