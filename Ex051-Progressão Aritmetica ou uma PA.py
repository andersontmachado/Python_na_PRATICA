primeiro=int(input('Primeiro Termo: '))
razao=int(input('A razão: '))
decimo=primeiro+(10-1)*razao
for c in range (primeiro,decimo+razao,razao):
    print('{}'.format(c),end= '->')
print('ACABOU')



