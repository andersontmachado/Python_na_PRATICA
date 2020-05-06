from time import sleep

print('\033[1;33m =-=\033[m' * 20)
print('\033[1;31m ANALIZANDO O TRIÂNGULO....\033[m')
print('\033[4;36m =-=\033[m' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))
sleep(2)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima \033[1;31mPODEM\033[m FORMAR TRIÂNGULO!')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos acima \033[1;35mNÃO\033[m PODEM FORMAR TRIÂNGULO!')
