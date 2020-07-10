soma= cont=0
while True:#Verdadeiro,sempre vai ser verdade,chama loop infinito,o break é para interromper
        n=int(input('Digite um valor (999 para sair): '))
        if n == 999:#se eu digitar 999 ele vai sair,e vai me retorna a soma dos valores
            break
        cont+=1 #vai contar os valores digitados.
        soma+=n #vai somar os valores
print(f'A Soma dos \033[31m{cont}\033[m valores foi de \033[32m{soma}\033[m')
#coloquei cores nas respostas.....








