
from datetime import date
ano=int(input('Em qual ano você quer analizar: Coloque 0 para o ano atual: '))
if ano ==0:
    ano=date.today().year
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print('O ano {} é \033[1;35m BISSEXTO\033[m'.format(ano))
else:
    print('O ano {} \033[1;32mnão\033[m é BISSEXTO'.format(ano))

