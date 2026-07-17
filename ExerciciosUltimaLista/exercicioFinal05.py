# Recebe uma quantidade (N) e um número de início e retorna uma lista com os primeiros N números primos a partir do número recebido (utilize sua função para obtenção do próximo número primo).
from funcaoVerificaPrimos import eh_primo


def aPatir(n, i):
    total = []
    ind = i
    while len(total) < n:
        if eh_primo(ind):
            total.append(ind)
            ind = ind + 1
        else:
            ind = ind + 1

    return total


print(aPatir(5, 10))
