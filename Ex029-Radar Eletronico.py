
velocidade=int(input('Qual a velocidade atual do carro? '))

if velocidade >80:
    #a velocidade acima de 80 sera imprimido a multa,então mais facil fazer a multa,do que o parabens.
    #não precisa colocar o else,pois sera uma condififcação simples.

    print('\033[1;31m Multado!Você excedeu o limite da pista que é de 80 km/h\033[m')
    multa=(velocidade-80)*7
    print('\033[1;31m Você deve pagar uma multa de \033[1;33mR${:.2f} \033[m'.format(multa))
print('\033[1;32m Tenha um bom dia! Dirija com segurança!')
