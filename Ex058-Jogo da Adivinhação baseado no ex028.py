from random import randint
from time import sleep

computador = randint(0, 5)
print('Sou seu computador....')
print('Acabei de pensar num número de 0 a 5!')
acertou = False
palpite = 0
opinião=''
while not acertou:
    jogador = int(input('Qual o seu palpite: '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...tente outra vez!')
        elif jogador > computador:
            print('Menos...Tente outra vez!')
opcão=str(input('Você tem certeza disso? [SIM ou NÃO]')).strip().upper()[0]
if opcão not in 'N':
    print('Sua opinião foi {},Será?'.format(opcão))
    print('Sabe muito!')
    sleep(2)
    print('\033[34mAcertou com {} tentativas.PARABENS'.format(palpite))

else:
    print('Sua opinião foi {}\nJogo acabo'.format(opcão))
'''Esse jogo eu fiz baseado no curso em video,porem coloquei mais codigos,muito bom.'''





























