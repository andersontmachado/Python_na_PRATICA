resp = 'S'
soma=0
quant=0
media=0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma=soma+num
    quant+=1






    resp = str(input('Você quer continuar [S/N] ')).strip().upper()[0]
media=soma/quant


print('Você digitou {} numeros e a media foi {:.2f}'.format(quant,media))




