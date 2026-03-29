import random

def searchNumber(lista, n):

    if n in lista:
        print(f'O {n} está presente na lista. Sortudo!!')
        print(f'A posição do seu número na lista é {lista.index(n)}')
        return True


    else:
        print('Número não encontrado\nQue pena!!')
        return False

tentativas = 0
numeros = random.sample(range(1, 101), 10)
print('Vamos Testar a sorte!\nAbaixo teŕa uma lista de número aleatórios.\nTente acertar um número na lista! ')

while True:
    n = int(input('Insira seu número premiado: '))
    tentativas += 1

    hit = searchNumber(numeros, n)

    if hit:
        print(f'Você acertou em {tentativas} tentativa(s)')
        break

    elif n not in numeros and tentativas > 1:
        print(f'Caramba, já tentou {tentativas} e ainda nada, que azar!!')


    else:
        print(f'Não foi dessa vez, na próxima você acerta!')