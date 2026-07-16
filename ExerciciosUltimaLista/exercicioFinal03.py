#Recebe uma lista com números, encontra o maior número dessa lista e retorna uma nova lista com todos os números da lista original divididos pelo maior número. (utilize a função max do Python): 

def divirMaior(lista):
    listaDivid = []
    maiorNumero = max(lista)
    ind = 0
    while ind < len(lista):
        total = lista [ind] / maiorNumero
        listaDivid.append(total)
        ind = ind + 1
        
    return listaDivid
  
    
print(divirMaior([1,2,3,4,5,10,3,2])) 