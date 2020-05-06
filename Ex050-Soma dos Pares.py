soma=0
cont=0
somaim=0
contimp=0
for c in range(1,7):
    num=int(input('Digite o {} valor: '.format(c)))
    if num % 2==0:
        soma=soma+num
        cont=cont+1
    elif num % 2 ==1:
        somaim=somaim+num
        contimp=contimp+1
print('Foram digitados {} Impares e a Soma {}'.format(contimp,somaim))
print('Foram digitados {} Pares e a Soma {}'.format(cont, soma))

#esse exercicio era só SOMAR PAR eu como sou teimoso demorei uns 40 minutos,mais
#consegui fazer com IMPAR tambem e a soma,bateu tudo certo.)P




























