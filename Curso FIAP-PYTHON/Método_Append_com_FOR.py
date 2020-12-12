inventario = []
resposta = "S"
while resposta == "S":
    inventario.append(input("Equipamento: "))
    inventario.append(float(input("Valor:R$ ")))
    inventario.append(int(input("Número Serial: ")))
    inventario.append(input("Departamento: "))
    resposta = input("Digite \"S\" para continuar: ").upper()
"""a palavra APPEND é para ACRESCENTAR,então nesse código apliquei esse método
onde agente consegue adiciona o produto,o valor,a serial,departamento."""

for elemento in inventario:
    print(elemento)
"""Acrescenter o for,quando coloco N de não,ele imprimi o resultado do inventario."""

