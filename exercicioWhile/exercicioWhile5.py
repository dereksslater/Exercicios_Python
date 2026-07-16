# Apresente os múltiplos de um número em ordem crescente. Obtenha, via entrada do usuário, o número o qual deseja-se ver os múltiplos e o total de múltiplos a apresentar. Inicie a apresentação a partir do 1. Exemplo:
# 3; 4: resultado: 3 6 9 12

number1 = int(input("Digite o número que deseja ver o múltiplos: "))
number2 = int(input("Digite o total de múltiplos a apresentar: "))

cont = 1

while cont <= number2:
    print(number1 * cont)
    cont = cont + 1
