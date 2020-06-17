from datetime import date
atual=date.today().year
ano=int(input('Em que ano voce nasceu: '))
idade=atual-ano
print('Você tem {} anos'.format(idade))


