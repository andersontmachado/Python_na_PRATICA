from random import randint
numeros=(randint(1,10),randint(1,10),randint(1,10),
         randint(1,10),randint(1,10))
print(f'Os numero sorteados foram:\n',end='')
for n in numeros:
    print(n)
