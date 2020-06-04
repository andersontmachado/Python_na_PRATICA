'''n=int(input('Digite um número: '))
c=n
f=1
print('Calculando {}! '.format(n),end='')
while c>0:
    print('{}'.format(c),end='')
    print(' x 'if c>1 else'=' ,end='')
    f=f*c
    c=c-1
print(' {} '.format(f))'''
#fiz baseado no curso o de cima,e agora,vou fazer um de fatorial e um com for.
'''from math import factorial
n=int(input('Digite um número: '))
c=n
f=factorial(n)
print('Calculando {}! '.format(n),end='')
while c>0:
    print('{}'.format(c),end='')
    print(' x 'if c>1 else'=' ,end='')
    c=c-1
print(' {} '.format(f))'''
#farei um com for agora,pra praticar mais
numero = int(input('Digite um número para obter seu fatorial: '))
fatorial = numero

for n in range(1,numero):
    fatorial *= n
print(fatorial)

























