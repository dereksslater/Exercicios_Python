"""Solicite a quantidade de km percorridos e a quantidade de dias pelos quais um carro foi alugado. Calcule e apresente o preço a pagar, sabendo que o aluguel do carro custa R$ 60 por dia e R$ 0,15 por km rodado."""

kmperc = int(input("Digite o km percorrido: "))

dias = int(input("Digite os dias percorridos"))

valorKm = kmperc * 0.15
valorDia = dias * 60

total = valorDia + valorKm

print(f"O valor total a pagar pelo uso do carro é: R$ {total: .2f}")
