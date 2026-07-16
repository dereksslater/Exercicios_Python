"""Converter uma temperatura informada pelo usuário em Celsius para Fahrenheit e apresentá-la como saída. F =9  C5 + 32"""

valor = int(input("Digite o valor para ser convertido em Fahrenheit: "))

resultado = (9 * valor) / 5 + 32
print(f" O valor em Fahrenheit é: {resultado} ")
