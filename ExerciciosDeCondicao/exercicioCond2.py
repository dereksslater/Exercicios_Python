#Obtenha dois valores numéricos via entrada do usuário e apresente um valor Lógico indicando se ambos números são positivos. 
#Exemplo: num1 → 1, num2 → 4, apresenta True
#Exemplo: num1 → 1, num2 → -5, apresenta False

num1 = int(input("Digite o primeiro número"))
num2 = int(input("Digite o segundo número"))

if num1 >= 0 and num2 >= 0:
    print("True")
else:
    print("False")
        