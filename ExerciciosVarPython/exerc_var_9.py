'''Calcule e exiba o tempo de uma viagem de carro. Pergunte a distância a percorrer (em km) e a velocidade média (em km/h) esperada para a viagem. Apresente o tempo de viagem (em horas) com apenas uma casa decimal.'''

distancia = int(input("Qual a distância km da viajem? "))

velociadade = int(input("Qual a velocidade média em km da viajem? "))

resultado = distancia / velociadade

print(f"Tempo de viajem estimado:{resultado: .1f} horas")


