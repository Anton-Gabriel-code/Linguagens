a_hora = float(input("Insira o quanto ganha por hora: "))

tempo = float(input("Insira quantas horas foram trabalhadas no mês: "))

salario_bruto = a_hora * tempo

ir = (salario_bruto * 11)/100

inss = (salario_bruto * 8)/100

sindicato = (salario_bruto * 5)/100

salario_liquido = salario_bruto - ir - inss - sindicato

print(f"Esse é o seu salário bruto sem os descontos R$ {salario_bruto:.2f}")

print(f"Esses são os valores que foram descontados do seu salário:\nIR: R${ir:.2f}\nINSS: R${inss:.2f}\nSindicato: R$ {sindicato:.2f}")
print(f"Esse é o seu salário após os descontos: R${salario_liquido:.2f}")