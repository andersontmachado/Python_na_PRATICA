print('Gerador de uma PA')
print('=-'*10)
primeiro=int(input('Primeiro termo: '))
razão=int(input('Razão da P.A: '))
termo=primeiro
cont=1
while cont <=20:
    print('{}->'.format(termo),end='')#tiramos o final da linha..
    termo=termo+razão
    cont+=1
print('FIM')
