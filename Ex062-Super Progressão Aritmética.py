print('Gerador de uma PA')
print('=-'*10)
primeiro=int(input('Primeiro termo: '))
razão=int(input('Razão da P.A: '))
termo=primeiro
#criamos uma vriavel pro termo,vai começar com o pimeiro termo
cont=1
#vai contar quantos termos foram, no exercicio 51 tivenmos que criar,aqui nao precisa.
while cont <=20:#enquanto ele não chegar a 10,vai mostra o termo
    print('{}->'.format(termo),end='')#tiramos o final da linha..
#ele vai mostra alguma coisa e uma setinha vai ser o meu termo
    termo=termo+razão
#termo seja o termo mais a razaão simplificada
    cont+=1

print('FIM')
#pra acabar
