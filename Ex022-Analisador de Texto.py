'''n=str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome......')
print('Seu nome em maiuscula é {}'.format(n.upper()))
print('Seu nome em minuscula é {}'.format(n.lower()))
print('Seu nome tem {} letras'.format(len(n) - n.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(n.find(' ')))
separa=n.split()
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))'''

n=str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome....')
print('Seu nome em maiuscula  é {}'.format(n.upper()))
print('Seu nome em minuscula é {}'.format(n.lower()))
print('Seu nome ao todo tem {} letras'.format(len(n) - n.count(' ')))
#print('Seu primeiro nome tem  {} letras '.format(n.find(' ')))
separa= n.split()
print(separa) #coloquei esse elemento para ver a separação dos nome.
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))

