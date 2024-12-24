#   Faça um algoritimo que leia o salário de um funcionário e mostre
#   seu novo salário, com 15% de aumento.
s = float(input('Qual é o salário do funcionário? R$'))
s = s + (s * (15/100))
print('Funcionário passará a ganhar R${:.2f}'.format(s))
