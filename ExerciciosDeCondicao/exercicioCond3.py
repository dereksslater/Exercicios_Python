# Obtenha um valor numérico via entrada do usuário e apresente um valor Lógico indicando se o valor está no intervalo 0<x<1. Separe a verificação em duas partes (utilizando um operador lógico).

numb = float(input("Digite um número: "))

if numb > 0 and numb < 1:
    print(f" O valor {numb} está dentro de 0 a 1")
else:
    print(f" O valor {numb} não esta dentro de 0 a 1")
