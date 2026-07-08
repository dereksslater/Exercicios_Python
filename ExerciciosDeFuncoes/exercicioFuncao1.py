#1. Verifique se um número está dentro de um intervalo, portanto, a função recebe três parâmetros: o início do intervalo, o fim do intervalo e o número a ser testado. Retorna verdadeiro caso pertença ao intervalo e falso caso contrário.



def intervalo (a, b, c):
 
 if c > a and c < b:
      return True 
 else:
     return False
     
 
print(intervalo (3 , 11, 10))
print(intervalo (3 , 16, 19))
print(intervalo (3 ,6, 4))

