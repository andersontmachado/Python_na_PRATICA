# MANEIRA UM: TAMBEM ESTA CERTA,POREM A SEGUNDA VAI SER MAIS SIMPLIFICADA.VEJA
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
if a < b and a < c:
    menor = a
if b < c and b < a:
     menor = b
if c < a and c < b:
    menor = c
print('O  menor valor é {}.'.format(menor))

#LEMBRE-SE TUDO QUE ESTA DO LADO ESQUERDO O PROGRAMA VAI EXECUTAR!!!!!! POR ISSO QUE ESTAVA
#ERRANDO,COLOQUEI O PRINT 3 VEZES,NA VERDADE SÓ UM VEZ JA BASTA,BASTA COLOCAR DO LADO ESQUERDO O PRINT
# TEMOS OUTRA MANEIRA:
'''a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O menor valor é {}'.format(menor))'''
#SÓ COM 2 IF,MANEIRA MAIS SIMPLES.

