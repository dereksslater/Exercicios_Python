#Obtenha dois valores numéricos via entrada do usuário e apresente um valor Lógico indicando se o segundo valor informado é maior do que o primeiro.
#Exemplo: num1 → 5, num2 → 9, apresenta True
#Exemplo: num1 → 5, num2 → -1, apresenta False

num1 = int(input("Digite o primeiro valor"))

num2 = int(input("Digite o segundo valor"))

if num2 > num1:
    print("True")
else:
    if num2 < num1:
        print("False")
        