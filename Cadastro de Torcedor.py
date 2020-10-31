from time import sleep
print('-='*25)
print(f'{"UNICID-CADASTRO DO TORCEDOR":^40}')
print('-='*25)
print(f'{"PROJETO INTEGRADO EM ANÁLISE E DESENVOLVIMENTO DE SISTEMAS"}')
print('*'*60)
sleep(1)
ingresso=c=0
cpf=str
opção=' '
while True:
    torcedor=str(input('Digite seu Nome e Sobrenome: ').strip().upper())
    print(f'Bem vindo {torcedor}')
    idade=int(input('Quantos anos você tem? '))
    cpf=str(input('Digite seu cpf: ').strip())
    if len(cpf)<11:
        cpf=cpf.zfill(11)
    tamanho_cpf =str(input('{}.{}.{}-{}'.format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])))
    if len(cpf)>11:
        print('CPF INVÁLIDO')
        break
    while True:
        ingresso=int(input('Deseja quantos ingressos: '))
        if ingresso > 0 and ingresso <=3:
            print('Válido')
        else:
            print('Inválido! Tem direito você e mais duas pessoas!')
    while True:
        print('''Os Ingressos disponiveis são: 
         [1]Arquibancada
         [2]Numeradas
         [3]Camarotes
         [4]Sair''')
        opção=str(input('Qual sua opção: '))
            if opção ==1:
            ingresso_arq=str('O Ingresso para arquibancada custará R$30,00 Aceita[S/N]')
            if opção == 'Ss':
            quantos_ingresso=str(input('Quantidade?'))
            else:
                break
print('Tente Novamente....')



