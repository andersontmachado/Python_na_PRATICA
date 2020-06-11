n=0
cont=0
soma=0
n = int(input('Digite um número [999 para parar]: '))#copia de dois codigos,isso tudo eh uma gambiarra
while n != 999:
    soma+=n
    cont+=1
    n = int(input('Digite um número [999 para parar]: '))#gambiarra para não somar o 999 junto e os valores.
print('Você digitou {} números e a soma é {}'.format(cont,soma))
print('FIM')

'''quando se a variaveis iguais a zer,como está,pode se colocar assim:
n=cont=soma=0,em umal inha só,eu fiz de três,pq ja sou acostumado.

#haverá um jeito mais facil de resolver essa aula,na proxima aula,então não vo
muito me aperfeiçoar desse jeito'''









