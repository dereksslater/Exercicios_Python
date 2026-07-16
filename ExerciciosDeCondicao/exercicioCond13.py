# Obtenha dois valores numéricos via entrada do usuário e apresente qual dos dois valores é o maior. Caso os valores sejam iguais, avise o usuário e não informe qual número é o maior.
valor1 = int(input("Digite o primeiro número: "))
valor2 = int(input("Digite o segundo número: "))

if valor1 > valor2:
    print(f"O valor {valor1} é maior que o {valor2}")

elif valor1 < valor2:
    print(f"O valor {valor2} é maior que o {valor1}")

elif valor1 == valor2:
    print("Os valores são iguais")
