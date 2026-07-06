#Obtenha um número inteiro maior do que 0, esse número indica a quantidade de caracteres que serão exibidos diretamente (na mesma linha, separados por espaço). Os caracteres exibidos são A, B e C, nessa ordem. A cada 3 caracteres A mostrados, troca-se para B, após 3 B’s, troca-se para o C e, finalmente, após 3 C’s, o programa volta a exibir A e o ciclo continua. Ao final, o método mostra quantos caracteres A, B e C foram exibidos e retorna quantos B foram exibidos.
#obs.: para exibir os caracteres na mesma linha, utilize o recurso de concatenação de Strings e mostre a String resultante no final. Exemplo:
#resultado = ‘A’
#resultado = resultado + ‘A’
#resultado = resultado + ‘B’
#print(resultado) → saída: AAB
#obs2.: se preferir, também é possível utilizar a abordagem do exercício Fibonacci, disponível no Moodle.

n = int(input("Quantos caracteres? "))

resultado = ""
letra = "A"        
repeticoes = 0     
cont_A = 0
cont_B = 0
cont_C = 0

i = 0
while i < n:
    resultado = resultado + letra + " "
    
  
    if letra == "A": cont_A = cont_A + 1
    if letra == "B": cont_B = cont_B + 1
    if letra == "C": cont_C = cont_C + 1
    
  
    repeticoes = repeticoes + 1
    
    if repeticoes == 3: 
        repeticoes = 0  
      
        if letra == "A": letra = "B"
        elif letra == "B": letra = "C"
        else: letra = "A" 
        
    i = i + 1

print(resultado)
print(f"A: {cont_A}, B: {cont_B}, C: {cont_C}")




