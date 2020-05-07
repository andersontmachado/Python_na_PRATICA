frase=str(input('Digite uma frase: ')).strip().upper()
palavras=frase.split()
junto=''.join(palavras)
inverso=junto[::-1]
print('O inverso de {} é {}'.format(junto,inverso))
if inverso == junto:
    print('TEMOS um palindromo')
else:
    print('NÃO temos um palindromo')
''' Um palindromo quer dizer palavras que de traz pra frente são as mesma.
APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.'''



