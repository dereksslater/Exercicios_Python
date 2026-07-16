# Recebe uma lista de números e retorna o somatório dos números pares presentes na lista.


def somar_pares(lista):
    total = 0
    for num in lista:
        if num % 2 == 0:
            total = total + num

    return total


minha_lista = [1, 2, 3, 4, 5, 6, 4, 4, 7, 78, 22]


resultado = somar_pares(minha_lista)


print(resultado)
