# Recebe um número inteiro representando a quantidade de números aleatórios  desejados e retorna uma lista com essa quantidade de números inteiros produzidos aleatoriamente. Utilize alguma função do módulo random.
import random


def contadorAleator(quantidade):
    total = []
    ind = 0
    while ind < quantidade:
        numeroInteiro = random.randint(1, 100)
        total.append(numeroInteiro)
        ind = ind + 1

    return total


print(contadorAleator(5))
