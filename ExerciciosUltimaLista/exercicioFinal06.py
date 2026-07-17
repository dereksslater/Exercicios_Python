# Recebe duas listas e retorna uma nova lista contendo a multiplicação dos elementos com o mesmo índice das listas de entrada. Caso o tamanho das listas seja diferente, inclua diretamente os elementos restantes da maior lista.


def listaMultiplica(lista1, lista2):
    novaLista = []
    ind = 0
    while ind < len(lista1) and ind <len(lista2):
        multipli = lista1[ind] * lista2[ind]
        novaLista.append(multipli)
        ind = ind + 1
    while ind < len(lista1):
        
        novaLista.append(lista1[ind])
        ind = ind +1
        
    while ind < len(lista2):
        
        novaLista.append(lista2[ind])
        ind = ind + 1
        
                
    return novaLista     

    


print(listaMultiplica([1,2,3,4,5,6,7],[1,2,3,4,5,6,7,8,6]))
