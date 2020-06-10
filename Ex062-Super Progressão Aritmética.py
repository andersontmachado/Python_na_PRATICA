print('Gerador de uma PA')
print('=>'*10)
primeiro=int(input('Primeiro termo: '))
razão=int(input('Qual a razaão da PA: '))
termo=primeiro
cont=1
total=0
mais=5
'''esse qui é o termo que vai contar agora,como não sabiamos o que o usuario
 iria digitar,fazemos uma variavel total e depois  criamos no while'''

while mais !=0:
    total+=mais
    while cont<=total:
        print('{}->'.format(termo),end='')
        termo=termo+razão
        cont=cont+1

    print('PAUSA')
    mais=int(input('Quantos termo você quer a mais: '))

print('Progressão finalizada com {} termos.'.format(total))

'''tentei brincar colocando o que o usuario digitou se é par ou impar,mais não consegui.
irei tentar mais pra frente.'''
























