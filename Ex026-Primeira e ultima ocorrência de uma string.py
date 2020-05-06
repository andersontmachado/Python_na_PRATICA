frase=str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
#acrescentando o +1 A POSIÇÃO MUDA PARA UMA A MAIS,o normal seria posição 0.
print('A ultima letra A apareceu na posição {}'.format(frase.rfind('A')+1))
#Mesmo esquema do exemplo acima,foi acrescentado uma posição +1
# rfind é o código para contar da direita pra esquerda









