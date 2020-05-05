salario=float(input('Qual é o salário do funcionario R$'))
novo=salario+(salario*15/100)
print('Um funcionário que ganhava {:.2f} com aumento de 15%,passa a receber R${:.2f}'.format(salario,novo))
#