# Tendo como dados de entrada um arquivo em Gigabytes, construa um algoritmo que faça a conversão para Megabytes, usando a seguinte fórmula:
#Giga * 1024


giga = float(input("Insira o valor em Gigabytes para coversão: "))

mega = giga * 1024

print(f"Esse é o valor de Gigabytes -> Megabytes: {mega:.0f}")