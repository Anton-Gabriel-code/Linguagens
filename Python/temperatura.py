# Faça um programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# Faça um programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

#formulas: C = 5 * ((F-32) / 9) | F = (C * 9/5) + 32

print("=" * 50)
print("Calculadora de conversão de temperatura")
print("=" * 50)

Faher = float(input("Insira uma temperatura em Fahrenheit: "))

Cel = float(input("Insira uma temperatura em Celsius: "))

tempC = 5 * ((Faher - 32)/ 9)

tempF = (Cel * 9/5) + 32

print(f"Aqui estão as temperaturas inseridas nas suas denomidas conversões;\n Fahrenheit -> Celsius = {tempC:.1f}°C\nCelsius -> Fahrenheit = {tempF:.1f}°F")