# Recebe uma lista de números e um número qualquer e retorna um valor lógico indicando se o número está presente na lista.


def presente_na_lista(verifica):
    ind = 0
    lista = [2, 3, 4, 3, 2, 5, 6, 3, 5, 6, 8]

    while ind < len(lista):
        if verifica == lista[ind]:
            return True

        elif verifica != lista[ind]:
            ind = ind + 1

    return False


print(presente_na_lista(4))
