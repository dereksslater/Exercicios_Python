# Obtenha dois valores numéricos inteiros (N1 e N2), ambos maiores do que 0, e calcule o produtório de N1 até N2. Exiba o resultado do produtório e também informe se o resultado é par ou ímpar. Exemplo:
# N1: 3; N4: 7; resultado: 2520 → 3x4x5x6x7

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

cont = n1
produto = 1



while cont <= n2:
    print(cont)
    produto = produto * cont 
    cont = cont + 1
     
print(produto)

if produto %2 == 0:
    print("É par")
else:
    print("É ímpar")
    
    