from time import sleep
print('-='*25)
print(f'{"UNICID-CADASTRO DO TORCEDOR":^40}')
print('-='*25)
print(f'{"PROJETO INTEGRADO EM ANÁLISE E DESENVOLVIMENTO DE SISTEMAS"}')
print('*'*60)
sleep(2)
ingresso=0
cadastro=True
while True:
    torcedor=str(input('Digite seu Nome e Sobrenome: '))
    print(f'Bem vindo {torcedor}')
    idade=int(input('Quantos anos você tem? '))
    cadastro=int(input('Digite seu cpf: '))
    if cadastro == 11:
        print('Valido')
    else:
        print('Invalido')
    while True:
        ingresso=int(input('Deseja quantos ingressos: '))
        if ingresso > 0 and ingresso <=3:
            print('Válido')
            break
        else:
            print('Inválido! Tem direito você e mais duas pessoas!')
print('FIM')



