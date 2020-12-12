equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"
while resposta == "S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Número Serial: ")))
    departamentos.append(input("Departamento: "))
    resposta = input("Digite \"S\" para continuar: ").upper()


for equipamentos in equipamentos:
    print("Equipamento: ", equipamentos)
""" quando adiconamos o for,a resposta como NÃO,imprimi todos os equipoamentos digitados."""



