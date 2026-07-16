# Recebe uma lista com números e retorna um nova lista contendo os números primos presentes nessa lista. (utilize uma função para a verificação de primos assim como na lista 8).
from funcaoVerificaPrimos import eh_primo


def quantosPrimos(lista):
    quantidadePrimos = []
    ind = 0
    while ind <len(lista):
        if eh_primo(lista[ind]):
            quantidadePrimos.append(lista[ind])
        
        ind = ind + 1

    return quantidadePrimos
        



    
print(quantosPrimos([1,2,3,4,5,6,4,3,3,2,5,6,7,7,74,4,3,2]))