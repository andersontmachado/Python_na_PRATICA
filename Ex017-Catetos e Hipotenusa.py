'''co=float(input('Comprimento do cateto oposto: '))
ca=float(input('Comprimento do cateto adjascente: '))
h=(co**2+ca**2)**(1/2)
print('A hipotenusa vai medir {:.2f}'.format(h))'''

#dois metodos,com a biblioteca math e a biblioteca só de importar hypot


import math
co=float(input('Comprimento do cateto oposto: '))
ca=float(input('Comprimento do cateto adjascente: '))
hi=math.hypot(co,ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))


#ou da pra vc importar só o from math import hypot,depois na linha hi=hypot(co,ca)

