inventario=[]
resposta='S'
escola=[]
valores=[]
curso=[]
while resposta =='S':
    escola.append(input('Digite o nome da Escola: '))
    curso.append(input('Digite o nome do curso: '))
    valores.append(float(input('Digite o valor:R$ ')))
    resposta=input('Digite \'S\' para continuar: ').upper()


busca=input('Digite o nome da escola para busca: ')
for indice in range(0,len(escola)):
    if busca == escola[indice]:
        print('Nome.....',curso[indice])
        print('Valor R$ ',valores[indice])

for indice in range(0,len(escola)):
    print('Nome da Escola: ',(indice+1))
    print('Escola...',escola[indice])
    print('Curso....',curso[indice])
    print('Valor....',valores[indice])
    print('=-'*40)

desconto=input('Digite o equipamento que será descontado: ')
for indice in range(0,len(escola)):
    if desconto == escola[indice]:
        print('Valor antigo....',valores[indice])
        valores[indice]=valores[indice]*0.9
        print('Valor novo....',valores[indice])












