matriz=[[0,0,0],[0,0,0],[0,0,0]]#Criamos 3 listas,dentro delas pode se colocar o numero zero,em cada uma.
#agora fazemos um laço
for l in range(0,3):# dentro do for (l)linha faremos um outro for,agora para (c) coluna
    for c in range (0,3):
        #matriz=int(input(f'Digite um valor: '))#só que agora colocamos um (l) e o (c)
#       matriz[l][c]=int(input(f'Digite um valor: '))#testamos assim,depois coloque assim
        matriz[l][c]=int(input(f'Digite um valor para [{l},{c}]: '))
#print(matriz)#agora pra ficar BONITINHO,retiramos esse print mesmo
print('-='*30)
for l in range(0,3):
    for c in range(0,3):
#        print(f'[{matriz[l][c]}]',end='')
print(matriz)


