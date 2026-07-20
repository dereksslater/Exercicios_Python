# Recebe duas listas e retorna uma nova lista apenas com os elementos presentes em ambas listas.

def duasListas(lista1, lista2):
    total = []
    i = 0
    
    while i < len(lista1):
        j = 0  
        
        while j < len(lista2):
            if lista1[i] == lista2[j]:
                total.append(lista2[j])
                
            
            j = j + 1  
            
        i = i + 1  
        
    return total
        
print(duasListas([1,2,3,4,5,6],[3,2,1,5,4,7,6]))