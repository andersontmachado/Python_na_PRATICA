import math

angulo=float(input('Digite o ângulo que você deseja: '))
s=math.sin(math.radians(angulo))
print('O angulo tem {} tem o SENO de {:.2f} '.format(angulo,s))
c=math.cos(math.radians(angulo))
print('O angulo tem {} tem o COSSENO de {:.2f} '.format(angulo,c))
t=math.tan(math.radians(angulo))
print('O angulo tem {} tem a TANGENTE de {:.2f}'.format(angulo,t))

#ou também da pra importar só o from math import radinas,sin,cos,tan
#o math.sin ou cos ou tan tem que transformar em RADIANO,conveter para radiano.





