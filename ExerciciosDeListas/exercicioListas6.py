# Recebe duas listas de números e retorna o valor lógico verdadeiro caso a primeira lista tenha um somatório maior do que o da segunda lista. Para o cálculo do somatório utilize a função sum, já inclusa no Python.
def soma_e_compara(lista1, lista2):

    total1 = sum(lista1)

    total2 = sum(lista2)

    return total1 > total2


print(soma_e_compara([30], [1]))
