'''while True:
    t=int(input('Quer ver a tabuada de qual valor [0 para SAIR]: '))
    print('=-' * 30)
    if t == 0:#implementei o zero para sair,pois é nulo.
        break#vai parar quando digitar o zero
    for c in range(1,11):
        print(f'{t} x {c:2} = {t*c}')
print('PROGRAMA ENCERRADO')
...'''

opção=' '
while True:
    if opção not in 'NS':
        t=int(input('Quer ver a tabuada de qual valor: ').strip().upper()[0])
    print('=-' * 30)
    opção=str(input('Quer sair: [S/N]'))
    if opção in 'Nn':
        t=int(input('Quer ver a tabuada de qual valor: '))
    elif opção in 'Ss':
        break
    for c in range(1,11):
        print(f'{t} x {c:2} = {t*c}')

print('PROGRAMA ENCERRADO!')


#programa fiz com resposta para não sair e sair,esta 99% certo,só que ele
#da uma resposta no final com o numero da tabuada,não conseguii tirar.'''

