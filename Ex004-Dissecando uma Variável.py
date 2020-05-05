a=(input('Digite algo: '))
print('O valor primitivo desse valor é ',type(a))
print('Só tem espaços? ',a.isspace())
print('É um número? ',a.isnumeric())
print('É alfabético',a.isalpha())
print('É alfanumérico? ',a.isalnum())
print('Esta em minuscula? ',a.islower())
print('Esta em Maiuscula? ',a.isupper())
print('Esta capitalizada? ',a.istitle())
'''a=(input('Digite algo: '))
print('O valor primitivo desse valor é {} '.format(type(a)))
print('Só tem espaços? {} '.format(a.isspace()))
print('É um número? {} '.format(a.isnumeric()))
print('É alfabético? {}'.format(a.isalpha()))
print('É alfanumérico? {} '.format(a.isalnum()))
print('Esta em minuscula? {} '.format(a.islower()))
print('Esta em Maiuscula? {} '.format(a.isupper()))
print('Esta capitalizada? {} '.format(a.istitle()))'''

#existem duas formas,uma com o format e outra sem
#para acrescentar o format é necessario colocar as chaves,e .format,colocar o objeto a.isspace etc entre parenteses do format