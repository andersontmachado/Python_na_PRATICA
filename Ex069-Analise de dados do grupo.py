total18=0
totalh=0
totalm=0
total20=0
while True:
    idade=int(input('Idade: '))
    sexo=' '
    while sexo not in 'MF':
        sexo = str(input('Sexo:[M/F] ').strip().upper()[0])
    if idade >=18:
        total18+=1
    if sexo == 'M':
        totalh+=1
    if sexo == 'F' and idade <20:
        totalm+=1
    if sexo == 'F'and idade >=20:
        total20+=1

    resp=' '
    while resp not in 'SN':
        resp=str(input('Quer continuar:[S/N] ').strip().upper()[0])
    if resp == 'N':
        break
print(f'Temos {total18} pessoas maiores de 18 anos.')
print(f'Foram cadastrado {totalh} homens.')
print(f'Temos {totalm} mulheres com menos de 20 anos.')
print(f'Temos {total20} mulheres acima dos 20 anos.')










