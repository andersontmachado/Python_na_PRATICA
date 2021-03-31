'''pessoas=list()
pessoas.append('Gustavo')
pessoas.append(33)
galera=list()
galera.append(pessoas[:])
pessoas[0]='Anderson'
pessoas[1]='45'
galera.append(pessoas[:])
print(galera)
'''

#######################################################################################
'''galera=[['João',19],['Ana',33],['Joaquim',13],['Maria',45]]
print(galera)
print(galera[0])
print(galera[0][0])
print(galera[2][1])
print(galera[2][1])
'''
galera=[['João',19],['Ana',33],['Joaquim',13],['Maria',45]]
for p in galera:
    print(f'{p[0]} tem {p[1]} de idade')

