#Tendo como dados de entrada um arquivo em Gigabytes, construa um algoritmo que faça a conversão para Megabytes e Kilobytes, usando as seguintes fórmulas:
#Para Megabytes: Gigabytes * 1024
#Para Kilobytes: Gigabytes * 1024 * 1024


giga = float(input("Insira o valor em GigaBytes: "))

mega = giga * 1024

kilo = giga * 1024 * 1024

print(f"Esse é o valor de {giga:.0f}GB para\nMegaBytes: {mega:.0f}MB\nKiloBytes: {kilo:.0f}KB ")