num = list()
pares=list()
impares=list()
while True:
    num.append(int(input('Digite um numero: ')))
    resp = (input('Quer continuar: [S/N] '))
    if resp in 'Nn':
        break
for i,v in enumerate(num):
    if v % 2 ==0:
        pares.append(v)
    if v %2 == 1:
        impares.append(v)
print(f'Os valores digitados foram {num}')
print(f'Os valores de pares são {pares}')
print(f'Os valores digitados de impares são {impares}')

'''Exercicio bom e facil,só relembrar algumas funções ja consigo fazer varios desses.'''


