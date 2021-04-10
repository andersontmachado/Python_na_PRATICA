pessoas = list()
princ = list()
mai = men = 0
while True:
    pessoas.append(str(input('Nome: ')).upper())
    pessoas.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = pessoas[1]
    else:
        if pessoas[1] > mai:
            mai = pessoas[1]
        if pessoas[1] < men:
            men = pessoas[1]
    princ.append(pessoas[:])
    pessoas.clear()
    resp = str(input('Quer continuar: [S/N] '))
    if resp in 'Nn':
        break
# print(f'Os dados foram {princ}')Era só pr testar,não estava pedindo essa analise
print(f'Ao todo você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi {mai}kg', end=' ')
for p in princ:
    if p[1] == mai:
        print(f'O [{p[0]}]', end=' ')
print()
print(f'O menor peso foi {men}kg', end=' ')
for p in princ:
    if p[1] == men:
        print(f'O [{p[0]}]', end=' ')
print()
