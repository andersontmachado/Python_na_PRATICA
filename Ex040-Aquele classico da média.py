nota1=float(input('Primeira nota: '))
nota2=float(input('Segunda nota: '))
media=(nota1+nota2)/2
print('Tirando a nota {} e a {} a média é {}'.format(nota1,nota2,media))
if media >=5 and media <7:
    print('Você está em Recuperação!')
elif media <5:
    print('Você esta REPROVADO!')
else:
    print('Você está APROVADO!')






