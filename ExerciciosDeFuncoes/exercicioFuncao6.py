#Utilize a função criada no exercício 4 para calcular uma aproximação do número e utilizando a série infinita a seguir. O cálculo da aproximação recebe como parâmetro a quantidade de termos, portanto, deve ser um número maior do que 0. Caso seja menor ou igual a zero, retorna vazio.
import exercicioFuncao4


def infinite (a):
    if a <= 0:
        return 
    else:
        total = 0
        cont = 0
        while cont < a:
           resulFato = exercicioFuncao4.fatorial(cont)
           resultado = 1 / resulFato
           total = total + resultado
           cont = cont + 1
           
        return total
        

print(infinite(5))

    
    
