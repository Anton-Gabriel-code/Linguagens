# Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:

#O produto do dobro do primeiro com metade do segundo .
# A soma do triplo do primeiro com o terceiro.
#  O terceiro elevado ao cubo.

number1 = int(input("Insira 1 número inteiro: "))

number2 = int(input("Insira 1 número inteiro: "))

number3 = float(input("Insira 1 número real: "))

op1 = (number1 * 2) * (number2/2)

op2 = (number1 * 3) + number3

op3 = (number3)**3

print(f"O produto do dobro do primeiro com metade do segundo: {op1:.2f}\nA soma do triplo do primeiro com o terceiro: {op2:.2f}\nO terceiro elevado ao cubo: {op3:.1f}")
