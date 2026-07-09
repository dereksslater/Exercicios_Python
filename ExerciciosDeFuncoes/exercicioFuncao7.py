#Utilize a função criada no exercício 4 para calcular uma aproximação do cosseno utilizando a série infinita a seguir. O cálculo da aproximação recebe como parâmetro a quantidade de termos e o valor de x (entre 0 e 1), portanto, deve ser um número maior do que 0. Caso seja menor ou igual a zero, retorna vazio.
import math
import exercicioFuncao4  


def aproximar_cosseno(quantidade_termos, x):
    
    if x <= 0 or x > 1 or quantidade_termos <= 0:
        return None

    
    resultado_cosseno = 0.0

    
    n = 0

    
    while n < quantidade_termos:

        
        auxiliar_par = 2 * n

        
        sinal = (-1) ** n

        
        potencia_x = x**auxiliar_par

        fatorial_divisor = exercicioFuncao4.fatorial(auxiliar_par)

        
        termo_atual = (sinal * potencia_x) / fatorial_divisor

        
        resultado_cosseno = resultado_cosseno + termo_atual

        
        n = n + 1

    
    return resultado_cosseno


print(aproximar_cosseno(3,0.5))