cont=('zero','um','dois','três','quatro','cinco','seis','sete',
      'oito','nove','dez','onze','doze','treze','quatorze','quinze',
      'dezesseis','dezessete','dezoito','dezenove','vinte')
#foi digitado um por um por extenso,dai a posição que eu digitar
#no núm,vai ser o número por entenso 0 a 20.
while True:
    while True:
        núm = int(input('Digite um número de 0 a 20: '))
        if núm <=20:
            break
        print('Tente novamente...')
    print(f'O número digitado foi {cont[núm]}')
    opção=' '
    soma=0
    for c in range(0,21):
        while opção not in 'SN':
            opção = str(input('Quer continuar:[S/N] ').strip().upper()[0])
            if opção == 'S':
                núm=int(input('Digite umm número de 0 a 20: '))
                print(f'O número digitado foi {cont[núm]}')

            print('FIM')
