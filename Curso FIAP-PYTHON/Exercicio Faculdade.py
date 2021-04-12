pessoa = list()
princ = list()
mai = men = 0
for p in range(1, 4):
    pessoa.append(str(input('Aluno: ')).strip().upper())
    pessoa.append(float(input('Altura: ')))
    if len(princ) == 0:
        mai = pessoa[1]
    else:
        if pessoa[1] > mai:
            mai = pessoa[1]
    princ.append(pessoa[:])
    pessoa.clear()
print(f'Ao todo você cadastrou {len(princ)} pessoas.')
print(f'Altura maior é {mai}kg.Peso de ',end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}]',end='')
print()



#####Exercicio parece ser simples mais me deu um trabalhinho,porém rodo com sucesso
