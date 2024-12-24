# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu
# Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida
peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC da pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:  #professor colocou 18.5 <= imc < 25
    print('Peso ideal')
elif imc < 30:  #professor colocou 25 <= imc < 30
    print('Sobrepeso')
elif imc < 40:  #professor colocou 30 <= imc < 40
    print('Obesidade')
else:           #professor colocou elif imc >= 40
    print('Obesidade Mórbida')
