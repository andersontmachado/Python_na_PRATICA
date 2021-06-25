estados=list()
resp=''
while True:
    estados.append(str(input('Digite o Estado: ')).strip().upper())
    if resp in estados:
        print(f' O Estado {estados[0]} tem bastante gente com covid')






