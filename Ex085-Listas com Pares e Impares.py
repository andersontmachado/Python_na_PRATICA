num=[[],[]]
valor=0
for c in range(0,8):#Ultimo elemento ele não conta,só quero 7 elementos!!
    valor=int(input(f'Digite o {c}º valor: '))
    if valor%2==0:#quando o restante da divisão for 0,é par.
