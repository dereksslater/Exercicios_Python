# Obtenha dois valores numéricos via entrada do usuário e apresente qual dos dois valores é o maior. Considere que os valores são sempre diferentes entre si.
#Exemplo: num1 → 5, num2 → 9, apresenta O maior valor é o 9
#Exemplo: num1 → 5, num2 → -1, apresenta O maior valor é o 5

num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))

if num1 > num2:
    print(f"O maior valor é: {num1}")
elif num2 > num1:
    print(f"O mair valor é: {num2} ")
else:
    print(" Os valores são iguais ")