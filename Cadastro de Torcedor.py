from time import sleep
print('-='*25)
print(f'{"UNICID-CADASTRO DO TORCEDOR":^40}')
print('-='*25)
print(f'{"PROJETO INTEGRADO EM ANÁLISE E DESENVOLVIMENTO DE SISTEMAS"}')
print('*'*60)
sleep(1)
ingresso=c=0
cpf=str
while True:
    torcedor=str(input('Digite seu Nome e Sobrenome: ').strip().upper())
    print(f'Bem vindo {torcedor}')
    idade=int(input('Quantos anos você tem? '))
    cpf=str(input('Digite seu cpf: '))
    cpf=str
    tamanho_cpf=len(cpf)
    print(tamanho_cpf)






   """while True:
        ingresso=int(input('Deseja quantos ingressos: '))
        if ingresso > 0 and ingresso <=3:
            print('Válido')
            break
        else:
            print('Inválido! Tem direito você e mais duas pessoas!')
print('Tente Novamente....')"""


