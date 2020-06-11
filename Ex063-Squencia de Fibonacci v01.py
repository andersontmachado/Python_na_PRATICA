print('-'*25)
print('Frequencia de Fibonacci')
print('-'*25)
n=int(input('Quantos termos você quer mostrar: '))
print('-='*25)
t1=0
t2=1
print('{} -> {}'.format(t1,t2),end='')
cont=3#fizemos essa variavel para ja que tem t1 vale 0,t2 vale 1,criamos o contador com 3 em diante.
while cont <= n:
    t3=t1+t2#criamos o t3,pq o t1 vale 0, o t2 vale 1,pra poder fazer essa FREQUENCIA.ficam fixo
    print(' -> {}'.format(t3),end='')
#depois que foi feito essa do t3,eliminamos eles,ai o t1 passa a ser t2,t2 passa ser t3,e o t3 passar ser t1+t2,vai indo assim
    t1=t2
    t2=t3
    cont+=1#ir contando
print(' -> FIM')
''' Lembrando que não é contagem de todos os numeros,e sim do t1,t2,o t3 vale o t1+t2,ai como se contasse a e b,o c retorna
pra contar dinovo,exemplo...0->1->fixo,que valw t1=0,e t2=1,depois o t3 é o t1+t2,então na proxima sequencia,dá
0+1=1,a pfroxima sequencia 0+1=1+1=2+3=5+3=8 e assim por diante
                               -   -   -   -'''

























