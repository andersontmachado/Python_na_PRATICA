lista=[] #conjunto vazio
for c in range(0,5):
    n=int(input(f'Digite um valor: '))
    if c==0 or n>lista[-1]:#se ele é o primeiro ou maior que o ultimo
        lista.append(n)
        print('Adicionando ao final da lista...')
    else:
        pos=0
        while pos <len(lista):#vai da posição zero até a última
            if n < lista[pos]:
                lista.insert(pos,n)
                print(f'Adicionando na posição {pos} da lista')
                break
            pos+=1
print(f'Os valores digitados em ordem foram \033[1;32m{lista}\033[m')



