from datetime import date
from time import sleep
nome=input('Qual seu nome? ').upper()
idade=int(input('Qual sua idade? '))
time=input('Qual seu time: ').upper()
atual=date.today().year
anos_time=int(input('Em que anos seu time foi fundado: '))
resultado_anos=atual - anos_time
print(f'Seu nome é {nome}, tem {idade} anos,seu time é o \033[1;32m{time}\033[m,hoje dia 25 de Janeiro completa \033[1;33m{resultado_anos}\033[m de idade')
sleep(2)
print('\033[1;32mBORA COMEMORAR\033[m!!!!!')

#Vai mostra depois de dois segundos o BORA COMEMORAR
#Vai mostra as cores em BORA COMEMORAR




# MANDANDO ESSE PROGRAMINHA PARA MEU GIT HUB, FACIL...PORTIFOLIO....PROGRAMAR FAZ PARTE



