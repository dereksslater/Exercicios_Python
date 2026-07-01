'''Calcule o aumento de um salário. O programa deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário (com duas casas decimais apenas).
Exemplo 1: 
Qual o valor do salário atual? R$ 1900
Qual o percentual de aumento? 5
O salário com aumento de 5.0% é de R$1995.00
Exemplo 2:
Qual o valor do salário atual? R$ 7450.75
Qual o percentual de aumento? 13
O salário com aumento de 13.0% é de R$8419.35'''

salario = float(input("Qual o valor do salario atual? "))

percAumento = float(input("Qual o percentual de aumento? "))

total = salario * (1 + percAumento /100)

print(f"O salário com auemnto de {percAumento} é {total: .2f}")
