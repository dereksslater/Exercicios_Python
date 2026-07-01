'''Calcule a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro. Calcule e apresente a quantidade de dias já perdidos. '''
#10 min de vida por cigarro 
#1440

cigarrosDia = int(input("Quantos cigarros você fuma por dia? "))

anosFuma = int(input("Quantos anos você já fumou? "))

anosEmDias = cigarrosDia * 365 
totalCigarrofumados = anosEmDias * anosFuma

minutosPerdidos = totalCigarrofumados* 10

total = minutosPerdidos / 1440


print(f"Você perdeu {total: .1f} dias da sua vida") 

