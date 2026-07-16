"""Solicite o preço de um produto e o percentual de desconto. Exiba o valor do desconto e do preço a pagar (com apenas duas casas decimais)"""

produto = float(input("Digite o valor do produto: "))

percentualDesc = int(input("Qual o valor de desconto? "))

total = produto * (1 - percentualDesc / 100)

print(f"O valor de desconto foi: {percentualDesc}%")
print(f"Preço a pagar R$:{total: .2f}")
