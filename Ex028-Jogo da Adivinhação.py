'''from random import randint
from time import sleep
computador=randint(0,5)#Vai pensar num numero de zero até cinco
print('=-=' * 20)
print('Vou pensar num numero de 0 a 5. Tente adivinhar....')
print('=-=' *20)
jogador=int(input('Em que número eu pensei? '))
print('PROCESSANDO....')
sleep(2)
if jogador == computador:
    print('Parabens!Você me conseguiu me vencer.')
else:
    print('Ganhei! EU pensei no número {} e não no {}'.format(computador,jogador))'''
from random import randint
from time import sleep
computador= randint(0, 5)
print('Vou pensar em um número de 0 a 5.Tente Adivinhar....')
jogador=int(input('Eu pensei no número? '))
print('PROCESSANDO....')
sleep(2)
if jogador == computador:
    print('Parabens!Você conseguiu me vencer.')
else:
    print('Ganhei!Eu pensei no número {} e não no {}'.format(computador,jogador))

