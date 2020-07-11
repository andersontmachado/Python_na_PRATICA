opção=''
cont=0
while True:
    t=int(input('Quer ver a tabuada de qual valor: '))
    print('=-' * 30)
    for c in range(1,11):
        print(f'{t} x {c:2} = {t*c}')
opção=str(input('Quer sair? [S/N]').strip().upper()[0])
if opção in 'Nn':
    print('Quer ver a tabuada de qual valor: ')
elif opção in 'Ss':
    break
print('PROGRAMA ENCERRADO')