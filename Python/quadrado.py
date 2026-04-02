#Faça um programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.


altura = float(input("Insira a altura do quadrado: "))
base = float(input("Insira a base do quadrado: "))

area = base * altura

print(f"A área do seu quadrado é {area} e o dobro da sua área é {area * 2}")