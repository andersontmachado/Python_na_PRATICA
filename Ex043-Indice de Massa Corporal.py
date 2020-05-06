peso = float(input('Qual é o seu peso:(KG) '))
altura = float(input('Qual é sua altura:(m)'))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc <25: #sinal <= entre 18.5 e 25,o python aceita esssa sintaxe.
    print('Peso ideal')
elif 25<= imc <30:
    print('Sobrepeso')
elif 30 <= imc <40:
    print('Obesidade')
elif imc >= 40:
    print('Obesidade Mórbida')









