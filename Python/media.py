# Faça um programa que peça as 4 notas bimestrais e mostre a média. 
print("-"*60)
print("Bem vindo ao sistema de notas\nInsira abaixo a nota do aluno para que a média seja calculada")
print("-"*60)

nota1 = float(input("Nota da 1° prova: "))
nota2 = float(input("Nota da 2° prova: "))
nota3 = float(input("Nota da 3° prova: "))
nota4 = float(input("Nota da 4° prova: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f"A média final do seu aluno é {media:.2f}")