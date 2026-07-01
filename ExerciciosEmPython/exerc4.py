#Peça uma quantidade de minutos e mostre quantas horas e minutos sobram. Ex: 130 minutos → 2 horas e 10 minutos.

hrminutos = int (input("Digite o valor em minutos:"))
horas = hrminutos // 60
minutos = hrminutos % 60
print(horas,"horas e ", minutos,"minutos")

