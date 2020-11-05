from time import sleep
print('-='*25)
print(f'{"UNICID-CADASTRO DO TORCEDOR":^40}')
print('-='*25)
print(f'{"PROJETO INTEGRADO EM ANÁLISE E DESENVOLVIMENTO DE SISTEMAS"}')
print('*'*60)
sleep(1)
ingresso=c=0
cpf=str
opção=0
while True:
    torcedor=str(input('Digite seu Nome: ').strip().upper())
    sobreno=str(input('Digite seu sobrenome: ').strip().upper())
    print('Bem vindo {} {}'.format(torcedor,sobreno))
    idade=int(input('Quantos anos você tem? '))
    cpf=str(input('Digite seu cpf: ').strip())
    if len(cpf)<11:
        cpf=cpf.zfill(11)
    tamanho_cpf =str(input('{}.{}.{}-{}'.format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])))
    if len(cpf)>11:
        print('CPF INVÁLIDO')
        break
    while opção !=5:
        print('''Preços dos Ingresso:
          [1]ARQUIBANCADA
          [2]NUMERADA
          [3]CADEIRAS
          [4]SAIR''')
        opção = int(input('Qual sua opção: '))
        if opção ==1:
            print('Arquibancada você optou,custa R$30,00.')
            break
        elif opção==2:
            print('As numeradas custará R$50,00')
            break
        elif opção ==3:
            print('As cadeiras são mais caras,vão custar R$100,00')
            break
        elif opção ==4:
            break


print('saiu..')

