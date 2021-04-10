pessoa=list()
princ=list()
mai=men=0
for c in range(1,4):
    pessoa.append(str(input('Aluno: ')))
    pessoa.append(float(input('Altura: ')))
    if len(princ)==0:
        mai=men==pessoa[1]
    else:
        if pessoa[1]>mai:
            mai=pessoa[1]

    princ.append(pessoa[:])
    pessoa.clear()
   # print(f'Os dados foram {princ}')Era só pr testar,não estava pedindo essa analise
print(f'Ao todo você cadastrou {len(princ)} pessoas.')
print(f'A maior altura foi {mai}m', end=' ')




#####################
#Existe só um jeito de fazer isso, eu queria colocar o nome do aluno
#porem nao dá,tentei de tudo,nos foruns,consegue por só com tuplas ou listas
#ainda nao fiz



