cont=0
while True:
    t=int(input('Quer ver a tabuada de qual valor: '))
    print('=-' * 30)
    if t < 0:
        break
    for c in range(1,11):
        print(f'{t} x {c:2} = {t*c}')
print('PROGRAMA ENCERRADO')


'''opção=''
cont=0
while True:
    t=int(input('Quer ver a tabuada de qual valor: '))
    print('=-' * 30)
    for c in range(1,11):
        print(f'{t} x {c:2} = {t*c}')
    opção=str(input('Quer sair? [S/N]').strip().upper()[0])
    if opção in 'Nn':
        print(f'{t}')
    elif opção in 'Ss':
        break
print('PROGRAMA ENCERRADO!')
programa fiz com resposta para não sair e sair,esta 99% certo,só que ele
da uma resposta no final com o numero da tabuada,não conseguii tirar.'''

