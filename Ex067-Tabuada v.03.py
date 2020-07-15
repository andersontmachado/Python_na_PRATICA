'''while True:
    t=int(input('Quer ver a tabuada de qual valor [0 para SAIR]: '))
    print('=-' * 30)
    if t == 0:#implementei o zero para sair,pois é nulo.
        break#vai parar quando digitar o zero
    for c in range(1,11):
        print(f'{t} x {c:2} = {t*c}')
print('PROGRAMA ENCERRADO')
...'''
tipo=0
cont=0
opção=' '
while True:
    t=int(input('Quer ver a tabuada de qual valor: '))
    for c in range(1,11):
        print(f'{t} x {c:2} = {t*c}')
    opção: str(input('Quer sair:[S/N]'))












#programa fiz com resposta para não sair e sair,esta 99% certo,só que ele
#da uma resposta no final com o numero da tabuada,não conseguii tirar.'''

