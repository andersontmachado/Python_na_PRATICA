from time import sleep

print('\033[1;33m =-=\033[m' * 20)
print('\033[1;31m ANALIZANDO O TRIÂNGULO....\033[m')
print('\033[4;36m =-=\033[m' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))
sleep(3)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima \033[1;31mPODEM\033[m FORMAR TRIÂNGULO!')
else:
    print('Os segmentos acima \033[1;35mNÃO\033[m PODEM FORMAR TRIÂNGULO!')
'''Nesse exercicio foi muito bom,ele era básico,coloquei cores,coloquei para o computador
# dar aquela pensada,com tempo de 3 segundos com comando sleep importado.
##muito bom...VAMOS FAZER OS EXERCICIO OU VERFIFICAR NOVAMENTE,PARA PODER FAZER A PROVA'''