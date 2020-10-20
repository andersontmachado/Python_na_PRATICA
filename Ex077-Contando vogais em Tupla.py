palavras=('Anderson','Manoel','José','Maria','Zoraide','futebol','circo','voley','celular','chalé','cão')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos',end=' ')
    for letra in p:
        if letra.lower() in 'aàáâãéèêeiíìóòôouùúü':
            print(letra,end=' ')


##Exercicio um pouco simples,mais precisa prestar atenção,pq precisa de quebra de linha \n,precisa colocar as vogais com
#todos os tipos pra funcionar,o ideal seria colocar sem acento,mais como temos acentos em varias palavras,utlizamos esse metodo.
#precisar tranformar a palavra em maiuscula depois no final,le mostrar minuscula.



