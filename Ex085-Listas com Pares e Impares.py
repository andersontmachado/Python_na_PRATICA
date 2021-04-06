num=[[],[]]
valor=0
for c in range(1,8):#Ultimo elemento ele não conta,só quero 7 elementos!!
    valor=int(input(f'Digite o {c}º valor: '))
    if valor%2==0:#ou seja,quando o resto da divisão for zero,é par
        num[0].append(valor)
    else:
        num[1].append(valor)
print(f'Os valores pares foram {num[0]}.')
print(f'Os valores impares foram {num[1]}.')
