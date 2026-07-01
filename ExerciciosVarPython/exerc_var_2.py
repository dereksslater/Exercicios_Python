#Calcular e apresentar a área do trapézio a seguir obtendo os valores para base inferior (B), base superior (b) e altura (h) via entrada do usuário. Apresente mensagens para obtenção das entradas e para a saída.

infeB = float(input("Digite o valor da base inferior: "))
infeb = float(input("Digite o valor da base superior: "))
altura = float(input("Digite a altura: "))

resultado = (infeB + infeb) * altura /2

print(f"O resultado da área do trapézio é {resultado}")