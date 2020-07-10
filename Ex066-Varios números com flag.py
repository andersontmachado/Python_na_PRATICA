soma= cont=0
while True:
        n=int(input('Digite um valor (999 para sair): '))
        if n == 999:
            break
        cont+=1
        soma+=n
print(f'A Soma dos \033[31m{cont}\033[m valores foi de \033[32m{soma}\033[m')
#coloquei cores nas respostas.....








