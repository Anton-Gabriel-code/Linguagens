# Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

a_hora = float(input("Insira o quanto ganha por hora: "))

tempo = float(input("Insira quantas horas foram trabalhadas no mês: "))

salario = a_hora * tempo

print(f"Esse é o seu salário sem os descontos R$ {salario:.2f}")