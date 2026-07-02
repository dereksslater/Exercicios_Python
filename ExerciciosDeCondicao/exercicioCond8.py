#Calcular e apresentar a hipotenusa do triângulo abaixo obtendo os valores dos catetos via entrada do usuário. 
#Para obtenção dos valores, apresente a mensagem: Informe o valor do cateto N: → N indica qual cateto deve ser informado.  Caso os valores informados sejam negativos, exiba uma mensagem de aviso e não realize o cálculo.
#Para mostrar o resultado, apresente a seguinte mensagem: A hipotenusa é: R → R é o resultado do cálculo. 

cat1 = int(input("Informe o valor do cateto 1: "))
cat2 = int(input("Digite o valor do cateto 2: "))

if cat1 < 0 or cat2 < 0:
    print(" erro: número negativo")
else:
 resultado = (cat1 ** 2) + (cat2 **2) 
 raiz = resultado ** 0.5
 print(f"A hipotenusa é:{raiz}")
 
 
    
    