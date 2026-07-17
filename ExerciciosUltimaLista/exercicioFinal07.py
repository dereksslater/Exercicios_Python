# Recebe uma lista de tamanho par e maior do que 0 (caso não seja, retorne vazio) e, em seguida, troque o primeiro elemento com o último, o segundo com o penúltimo, o terceiro com o antepenúltimo, e assim sucessivamente. Retorne uma nova lista com as trocas realizadas.



def trocas(lista):
    listaNova = []
    ind = -1
    
    if len(lista) % 2 == 0 and len(lista) > 0:
   
        while len(listaNova) < len(lista):
            ultimo = lista[ind]
         
            listaNova.append(ultimo)
            ind = ind - 1
        
    else:
       
        return []

    return listaNova

print(trocas([1, 2, 3, 4, 5, 6, 7, 8]))