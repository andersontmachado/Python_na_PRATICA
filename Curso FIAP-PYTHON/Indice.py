equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"
while resposta == "S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor:R$ ")))
    seriais.append(int(input("Número Serial: ")))
    departamentos.append(input("Departamento: "))
    resposta = input("Digite \"S\" para continuar: ").upper()

for indice in range(0,len(equipamentos)):
    print("\nEquipamento..: ", (indice+1))#0+1=1
    print("Nome.........: ", equipamentos[indice])#nome refere-se ao equipamento,no indice 2
    print("Valor........:", valores[indice])
    print("Serial.......: ", seriais[indice])
    print("Departamento.: ", departamentos[indice])

#A variavel Indice que criamos no FOR,será atribuido o valor 0 até a quantidade de elementos que existirem na lista equipamentos.