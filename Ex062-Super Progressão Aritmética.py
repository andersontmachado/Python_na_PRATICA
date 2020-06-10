print('Gerador de uma PA')
print('=>'*10)
primeiro=int(input('Primeiro termo: '))
razão=int(input('Qual a razaão da PA: '))
termo=primeiro
cont=1
total=0
mais=10
while mais !=0:
    total+=mais
    while cont<=total:
        print('{}->'.format(termo),end='')
        termo=termo+razão
        cont=cont+1
    print('PAUSA')
    mais=int(input('Quantos termo você quer a mais: '))
print('FIM')



