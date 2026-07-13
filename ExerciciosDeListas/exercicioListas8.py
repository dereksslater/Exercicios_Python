# Recebe uma lista com notas (valores em ponto flutuante) entre 0 e 10 e retorna uma lista contendo a média e a moda das notas. Para o cálculo da média e mediana, utilize funções do módulo statistics. Caso a lista contenha notas inválidas, não realize o cálculo e a função não retorna nada.
import statistics # mode, mean

def media_moda(lista):
    ind = 0
    while ind <len(lista):
     if lista[ind] <0 or lista[ind] >10:
         ind = ind + 1
         return None
     else:
         ind = ind + 1
                 
    moda = statistics.mode(lista)
    media = statistics.mean(lista)
    
    return [moda,media]
    
    
print(media_moda([2.3,5.4,3.4,5.5,5.5,2.3,5,10]))
print(media_moda([2.3,5.4,3.4,5.5,5.5,2.3,4,3,4,4,4,4]))