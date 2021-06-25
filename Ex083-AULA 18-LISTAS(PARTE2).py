pessoas=list()
pessoas.append('Marcio')
pessoas.append(33)
galera=list()
galera.append(pessoas[:])#copia
pessoas[0]='Jose'
pessoas[1]=55
galera.append(pessoas[:])
pessoas[0]='Anderson'
pessoas[1]=15
galera.append(pessoas[:])
galera.insert(0,'Mara')
print(galera)
#######################################################################################
'''galera=[['João',19],['Ana',33],['Joaquim',13],['Maria',45]]
print(galera)
print(galera[0])
print(galera[0][0])
print(galera[2][1])
print(galera[2][1])
'''
'''galera=[['João',19],['Ana',33],['Joaquim',13],['Maria',45]]
for p in galera:
    print(f'{p[0]} tem {p[1]} de idade')'''

