n=0
s=0
nome=''
while True:
    n=str(input('Digite algum nome:'))
    if n == 'José':
        break
    nome+=n
'''print('A  será {}'.format(n,s))
IREMOS aprender daqui adiante com F string,uma nova pep que o
python faz,não precida por format mais,colocamos f depois aspas.'''
print('Seu nome é {}'.format(n))


