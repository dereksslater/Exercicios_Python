# Obtenha via entrada do usuário uma quantidade de dias, horas, minutos e segundos. Calcule e apresente o total em segundos.
# Exemplo: Entrada: dias: 2; horas: 4; minutos: 40; segundos: 20
# Saída: Total em segundos: 189620s
# Entrada: dias: 0; horas: 1; minutos: 0; segundos: 20
# Saída: Total em segundos: 3620s

dia = int(input("Digite uma quantidade de dias"))

hora = int(input("Digite uma quantidade de horas"))

minutos = int(input("Digite uma quantidade de minutos"))

segundos = int(input("Digite uma quantidade de segundos"))


diaConversao = dia * 86400
horaConversao = hora * 3600
minutosConversao = minutos * 60

resultado = diaConversao + horaConversao + minutosConversao + segundos

print(f"Total: {resultado} segundos")
