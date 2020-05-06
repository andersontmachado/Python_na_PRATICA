from random import randint
from time import sleep
itens=('Pedra','Papel','Tesoura')
computador=randint(0,2)
print('''Suas Opções:
[0]PEDRA
[1]PAPEL
[2]TESOURA''')
jogador=int(input('Qual é sua jogada?'))
print('JÓÓÓÓÓÓÓÓÓÓ')
sleep(2)
print('KEEN')
sleep(1)
print('POU')
sleep(1)
print('=-'*11)
print('O computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador]))
print('=-'*11)
if computador == 0:#computador jogou PEDRA
    if jogador ==0:
        print('Empate')
    elif jogador ==1:
        print('Jogador Venceu')
    elif jogador ==2:
        print('Computador Venceu')
    else:
        print('JOGADA INVALIDA')

elif computador ==1:#computador jogou PAPEL
    if jogador ==0:
        print('Computador Vence')
    elif jogador ==1:
        print('Empate')
    elif jogador ==2:
        print('Jogador Vence')
    else:
        print('JOGADA INVÁLIDA')

elif computador ==2:#computador jogou TESOURA
    if jogador ==0:
        print('Jogador Vence')
    elif jogador ==1:
        print('Computador Vence')
    elif jogador ==2:
        print('Empate')

    else:
        print('JOGADA INVÁLIDA')












