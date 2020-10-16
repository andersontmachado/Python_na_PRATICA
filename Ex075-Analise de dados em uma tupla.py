numero=(int(input('Digite um número: ')),
        int(input('Digite segundo número: ')),
        int(input('Digite o terceiro número: ')),
        int(input('Digite o ultimo número: ')))
print(f'Você digitou os valor {numero}')
print(f'O valor 9 apareceu {numero.count(9)} vezes')
if 3 in numero:#senão colocamos o if e o else,e não digitar o 3,ele da erro,então tem que por.
    print(f'O valor 3 apareceu na {numero.index(3)+1}ªposição.')
else:
    print('0 valor 3 não foi digitado nenhuma vez.')
print('Os valores em pares foram ',end='')
for n in numero:
    if n % 2==0:
        print(n,end=' ')


