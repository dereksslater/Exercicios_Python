# Obtenha três valores numéricos via entrada do usuário e apresente um valor Lógico indicando se os valores foram informados em ordem crescente.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

Crescente = num1 <= num2 <= num3

if Crescente:
    print(
        f"Os valores foram digitado em ordem crescente, os valores foram: {num1},{num2},{num3}"
    )
else:
    print(
        f"Os valores não foram digitados em ordem crescente, os valores foram: {num1},{num2},{num3}"
    )
