n=str(input('Digite seu nome completo: ')).strip().lower()
nome=n.split()
#o split vai pegar o nome inteiro e vai fatiar,dividir o nome inteiro
print('Muito prazer em te conhecer {}!\nSEJA BEM VINDO.'.format(n))
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[len(nome)-1]))

