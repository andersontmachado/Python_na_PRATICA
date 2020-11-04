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
    torcedor=str(input('Digite seu Nome: ').strip().upper())
    sobreno=str(input('Digite seu sobrenome: ').strip().upper())
    print(f'Bem vindo {torcedor,sobreno}')
    idade=int(input('Quantos anos você tem? '))
    cpf=str(input('Digite seu cpf: ').strip())
    if len(cpf)<11:
        cpf=cpf.zfill(11)
    tamanho_cpf =str(input('{}.{}.{}-{}'.format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])))
    if len(cpf)>11:
        print('CPF INVÁLIDO')
        break
while opção !=4:
