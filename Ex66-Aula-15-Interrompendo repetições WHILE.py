n=0
s=0
while True:
    n=int(input('Digite um número:'))
    if n ==999:
        break
    s+=n
'''print('A soma de {} será {}'.format(n,s))
IREMOS aprender daqui adiante com F string,uma nova pep que o
python faz,não precida por format mais,colocamos f depois aspas.'''
print(f'A SOMA DO VALOR {n} É {s}')

