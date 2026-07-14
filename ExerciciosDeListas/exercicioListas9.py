# Dado um gabarito de uma prova com 10 questões cujas respostas podem ser A, B, C, D ou E, elabore uma função que receba uma prova por parâmetro e retorna a quantidade de acertos. Gabarito: A,A,C,E,D,B,C,E,B,D. 

def prova(lista):
   
    gabarito = ["a","a","c","e","d","b","c","e","b","d"]
    acertos = 0
    ind = 0

    while ind < len(lista):
      
        if lista[ind] == gabarito[ind]:
            
            acertos = acertos + 1
        
        
        ind = ind + 1
        
    
    return acertos
        
print(prova(["a","a","c","b","e","b","c","e","c","e"]))


  
  






  

    
    
 