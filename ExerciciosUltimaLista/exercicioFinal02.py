# Recebe uma lista com números e retorna uma nova lista com o módulo de cada elemento da lista original.


def modulo(lista):
    novaLista = []
    ind = 0
    while ind < len(lista):
        if lista[ind] <0:
         converte = lista[ind] * -1
         novaLista.append(converte)
         ind = ind + 1
        else:
            novaLista.append(lista[ind])
            ind = ind + 1
    
    return novaLista



print(modulo([2,3,4,5,-2,-4]))