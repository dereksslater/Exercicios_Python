# Recebe uma lista de números e retorna qual o maior número presente na lista.


def MaiorLista(a, b, c, d, e, f, g):
    lista = [a, b, c, d, e, f, g]
    ind = 0
    numeroMaior = lista[0]
    tam = len(lista)

    while ind < tam:
        if lista[ind] > numeroMaior:
            numeroMaior = lista[ind]
        ind = ind + 1

    return numeroMaior


print(MaiorLista(3, 2, 5, 6, 3, 5, 5))
