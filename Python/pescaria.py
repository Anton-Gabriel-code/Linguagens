print("Bem-Vindo a Verificação de pesca\nColoque o seu peixe na balança e insira o valor abaixo.")

peso = float(input("Insira aqui o peso em Kg: "))

limite = 50; multa = 4; excesso = 0

if peso > 50:
    excesso = peso -limite

    for i in range(1, int(excesso) + 1):
        multa += 4

        print(f"O seu peixe atingiu o excesso em Kg {i} | Multa por excesso:R${multa:.2f}")


print(f"O peso do seu peixe {peso}Kg")
print(f"Exesso: {excesso:.2f}")
print(f"O valor total da multa: R${multa:.2f}")
