valores=list()
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar [S/N]'))
    if resp in 'Nn':
        break

print('=='*30)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Valor no formato descrecente {valores}')
if 5 in valores:#coloquei ao contrario estava dando erro...ficar esperto...o 5 esta em valores:
    print(f'O numero 5 esta na lista...')
else:
    print(f'O valor 5 não está na lista...')

'''Esse exercicio foi muito simples,porem tive dificuldade,a base acertei,os nome,sort reverse eu sabia
valores.append eu sabia,nao precisa colocar quando a resposta for sim uma variavel,tipo...resp='S',nao precisa
'''



