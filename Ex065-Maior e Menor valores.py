resp = 'S'
soma=0
quant=0
media=0
maior=0
menor=0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma=soma+num
    quant+=1
    if quant ==1:
        maior=maior=num #numero vai ser igual o maior e o menor
    else:
        if num>maior:
            maior=num
        if num <menor:
            menor=num
#esses dois if's estão dentro do outro if quant ==1,aninhamento dentro do while
    resp = str(input('Você quer continuar [S/N] ')).strip().upper()[0]
media=soma/quant
print('Você digitou {} numeros e a media foi {:.2f}'.format(quant,media))
print('O maior valor digitado é {} e o menor {}'.format(maior,menor))




