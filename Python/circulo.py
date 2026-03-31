#Faça um programa que peça o raio de um círculo, calcule e mostre sua área:

print("=="*45)
print("Abaixo insira o valor do raio do seu círculo para calcularmos a área")
print("=="*45)


raio = float(input("Insira o valor do raio: "))

ar = 3.14 * (raio ** 2)

print(f"A área do seu círculo de raio {raio} é de {ar:.2f}cm²")