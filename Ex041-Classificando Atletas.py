from datetime import date

atual = date.today().year
nasc = int(input('Digite o ano de nascimento: '))
idade = atual - nasc
print('O atleta tem {} anos.'.format(idade))
if idade <= 3:
    print('Classificação:Nenem')
    print('Ainda não tem idade para participa')
elif idade <= 14:
    print('Classificação: Infantil')
elif idade <= 19:
    print('Classificação:Junior')
elif idade <= 25:
    print('Classificação: Senior')
else:
    print('Classificação:Master')
