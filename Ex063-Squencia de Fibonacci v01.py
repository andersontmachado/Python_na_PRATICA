print('Sequencia de Fibonacci')
print('-=' * 20)
n = int(input('Digite quantos termos você quer mostar: '))
print('-='*20)
t1 = 0 #sera fixo,começamos com zero
t2 = 1#pra fazer Fibonacci essa questao utilizamos o 0 e 0 1 no começo,fixo
print('{} -> {}'.format(t1,t2),end='')
cont=3
while cont <= n:
    t3 = t1 + t2#o t3 eh o t1 + t2
    print(' -> {}'.format(t3),end='')
    t1=t2 #t1 passa a ser o t2
    t2=t3 #o t2 passa a ser t3,vai andando,pra não fazer vários termos desse,ai entra o while
    cont+=1
print(' -> FIM')




















